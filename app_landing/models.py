from django.db import models

# Create your models here.


class Label(models.Model):
    class Meta:
        verbose_name = u'Метка'
        verbose_name_plural = u'Метки'

    title = models.CharField(max_length=200, db_index=True, unique=True, verbose_name=u'Название секции')
    seo_description = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(max_length=120, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    class Meta:
        verbose_name = u'Фотография поста'
        verbose_name_plural = u'Фотографии постов'
        ordering = ['title']
    title = models.CharField(u'Описание фото', db_index=True, max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d', blank=True, verbose_name=u'Изображение к посту',
                            max_length=180)
    file_preview = models.ForeignKey('self',  on_delete=models.SET_NULL, null=True, blank=True)
    seo_description = models.CharField(max_length=200, blank=True)
    seo_alt = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta:
        db_table = 'post_table'
        ordering = ['index']
        verbose_name = u'Название поста'
        verbose_name_plural = u'Название постов'

    title = models.CharField(max_length=200, unique=True, verbose_name=u'Название раздела', db_index=True)
    label = models.ForeignKey(Label, verbose_name=u'Метка', default='')
    slug = models.SlugField(max_length=200, db_index=True)
    text_post = models.TextField(u'Описание сервиса', blank=True, unique=False, null=False)
    image_post = models.ManyToManyField(Images, blank=True, related_name='image_post')
    seo_description = models.CharField(max_length=200, blank=True)
    index = models.PositiveSmallIntegerField(blank=True)
    icons = models.CharField(max_length=50, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Price(models.Model):

    class Meta:
        verbose_name = u'Название пакета услуг'
        verbose_name_plural = u'Название пакетов услуг'
    title = models.CharField(max_length=200, unique=True, db_index=True, verbose_name=u'Наименование пакета')
    label = models.ForeignKey(Label, verbose_name=u'Метка', default='')
    slug = models.SlugField(max_length=120, db_index=True)
    description = models.TextField(verbose_name=u'Описание пакета услуг')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Цена пакета')
    seo_description = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    icons = models.CharField(max_length=50, blank=True, default='')
    index = models.PositiveSmallIntegerField(blank=True, default=1)

    def __str__(self):
        return self.title


class SubPost(models.Model):
    post = models.ForeignKey(Post, related_name='post')
    post_support = models.CharField(max_length=200, blank=True, verbose_name=u'Поддержка сервиса')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_support


class Services(models.Model):

    class Meta:
        verbose_name = u'Сервис'
        verbose_name_plural = u'Сервисы'
        ordering = ['index']
        db_table = 'app_services'

    title = models.CharField(max_length=120, unique=True, verbose_name=u'Сервис')
    slug = models.SlugField(max_length=20, blank=True)
    post = models.ForeignKey(Post, related_name='post_service')
    label = models.ForeignKey(Label, related_name='label_services', null=True, blank=True, default='')
    description = models.TextField(blank=True, unique=False, verbose_name=u'Описание сервиса')
    icons = models.CharField(max_length=20, blank=True, unique=False, verbose_name=u'Иконка')
    image_service = models.ManyToManyField(Images, blank=True, verbose_name=u'Фото сервиса')
    index = models.PositiveSmallIntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Slider(models.Model):
    background = models.ManyToManyField(Images, related_name='background')


class Contact(models.Model):

    class Meta:
        verbose_name = u'Контакт'
        verbose_name_plural = u'Контакты'
    title = models.CharField(max_length=200, blank=True, verbose_name=u'Контакты')
    description = models.CharField(max_length=1200, blank=True, verbose_name=u'Описание')
    address = models.CharField(max_length=200, blank=True, verbose_name=u'Адрес')
    email = models.CharField(max_length=120, blank=True, verbose_name=u'e-mail')
    number = models.CharField(max_length=20, blank=True, verbose_name=u'Телефон')

    def __str__(self):
        return self.title


class Messages(models.Model):

    class Meta:
        verbose_name = u'Сообщение с сайта'
        verbose_name_plural = 'Сообщения с сайта'

    email = models.EmailField(max_length=120, blank=True, null=True, verbose_name='Email пользователя')
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name='Имя пользователя')
    message = models.TextField(blank=True, null=True, verbose_name='Сообщение')

    def __str__(self):
        return self.name
