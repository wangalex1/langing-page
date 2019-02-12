from django.shortcuts import render, redirect
from .models import *
from .forms import MessagesForm
from .decorators import check_recaptcha
from django.contrib import messages

# Create your views here.


def landing(request):
    context = dict()
    context['features_1_to_3'] = Post.objects.filter(label=2).order_by('index')[0:3]
    context['features_4_to_6'] = Post.objects.filter(label=2).order_by('index')[3:6]
    context['features_7'] = Post.objects.filter(label=2).order_by('index')[6]
    context['features_8'] = Post.objects.filter(label=2).order_by('index')[7]
    context['sub_post'] = SubPost.objects.filter(post=Post.objects.filter(label=2).order_by('index')[7].id)
    context['gallery'] = Post.objects.filter(label=3).all()
    context['price_post'] = Post.objects.filter(label=5).all()
    context['prices'] = Price.objects.filter(label=5).order_by('index')
    context['service_post'] = Post.objects.filter(label=6).all
    context['services'] = Services.objects.filter(label=6).order_by('index')
    context['service_1'] = Services.objects.filter(label=6).order_by('index')[0]
    context['service_2'] = Services.objects.filter(label=6).order_by('index')[1]
    context['service_3'] = Services.objects.filter(label=6).order_by('index')[2]
    context['service_4'] = Services.objects.filter(label=6).order_by('index')[3]
    context['background'] = Slider.objects.all()
    context['contact'] = Contact.objects.all()
    return render(request, 'home.html', {'context': context})


@check_recaptcha
def messages_info(request):
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'Ваше сообщение сохранено и в ближайшее время будет расмотренно менеджером')
            return redirect('/')
        else:
            messages.info(request, 'Проверьте корректность заполнения данных')
            return redirect('/')
    else:
        return redirect('/')
