from django.contrib import admin

from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'label', 'slug', 'text_post', 'seo_description',
                    'index', 'created', 'updated']
    list_filter = ['title', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'seo_description', 'seo_alt', 'created', 'updated', 'file', 'file_preview']
    list_filter = ['title', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


class PriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'description', 'seo_description', 'created', 'updated']
    list_filter = ['title', 'price', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}


class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'seo_description', 'created', 'updated']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(Images, ImagesAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(SubPost)
admin.site.register(Services)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Messages, MessagesAdmin)
