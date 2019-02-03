from django.shortcuts import render
from .models import *

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
