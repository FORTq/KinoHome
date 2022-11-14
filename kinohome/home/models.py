from django.db import models

# Create your models here.
from django.urls import reverse


class Production_year(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/production_year/{self.slug}/'

    class Meta:
        ordering = ['title']
        verbose_name = 'Дата выхода'
        verbose_name_plural = 'Дата выхода'


class Producer(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/producer/{self.slug}/'

    class Meta:
        verbose_name = 'Продюсер'
        ordering = ['title']
        verbose_name_plural = 'Продюсеры'


class Author(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    photo = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/author/{self.slug}/'

    class Meta:
        verbose_name = 'Автор'
        ordering = ['title']
        verbose_name_plural = 'Авторы'


class Country(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/country/{self.slug}/'

    class Meta:
        ordering = ['title']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Scenario(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/scenario/{self.slug}/'

    class Meta:
        ordering = ['title']
        verbose_name = 'Сценарист'
        verbose_name_plural = 'Сценаристы'


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/category/{self.slug}/'

    class Meta:
        ordering = ['title']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Kino(models.Model):
    name = models.CharField(max_length=144, blank=True, null=True, default=None, verbose_name='Название')
    trailer = models.CharField(max_length=1000, blank=True, null=True, default=None, verbose_name='Трейлер')
    content = models.CharField(max_length=2000, blank=True, null=True, default=None, verbose_name='Описание')
    urlss = models.URLField(max_length=200, blank=True, null=True, default=None, verbose_name='Ссылка на просмотр')
    grade = models.FloatField(blank=True, null=True, default=None, verbose_name='Оценка')
    producer = models.ManyToManyField(Producer, blank=True, default=None, related_name='producer', verbose_name='Продюсер')
    scenario = models.ManyToManyField(Scenario, blank=True, default=None, related_name='scenario', verbose_name='Сценарист')
    сountry = models.ManyToManyField(Country, blank=True, default=None, related_name='сountry', verbose_name='Страна')
    category = models.ManyToManyField(Category, blank=True, related_name='category', verbose_name='Жанры')
    production_year = models.ForeignKey(Production_year, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Год выпуска')
    photo = models.ImageField(upload_to='media/kino_images/')
    photo_background = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)
    photos = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)
    photos2 = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)
    photos3 = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')
    author = models.ManyToManyField(Author, blank=True, default=None, related_name='author', verbose_name='Автор')
    time = models.BigIntegerField(blank=True, null=True, default=None, verbose_name='Время')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'

    def get_absolute_url(self):
        return f'/kino/{self.slug}{self.pk}/'


class PopularKino(models.Model):
    title = models.CharField(max_length=144, blank=True, null=True, default=None)
    list_kino = models.ForeignKey(Kino, blank=True, on_delete=models.CASCADE, default=True, related_name='list_kino_popular')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список популярного'
        verbose_name_plural = 'Список популярного'


class RecommendationsKino(models.Model):
    title = models.CharField(max_length=144, blank=True, null=True, default=None)
    list_kino = models.ForeignKey(Kino, blank=True, on_delete=models.CASCADE, default=True, related_name='list_kino_rec')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список реков кино'
        verbose_name_plural = 'Список реков кино'



class TrendKino(models.Model):
    title = models.CharField(max_length=144, blank=True, null=True, default=None)
    list_kino = models.ForeignKey(Kino, blank=True, on_delete=models.CASCADE, default=True, related_name='list_kino_trend')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тренд'
        verbose_name_plural = 'Тренды'

class Sidebar(models.Model):
    title = models.CharField(max_length=144, blank=True, null=True, default=None, verbose_name='Заголовок')
    content = models.CharField(max_length=500, blank=True, null=True, default=None, verbose_name='Описание')
    photo = models.ImageField(upload_to='media/kino_images/', blank=True, null=True)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Сайдбар'
        verbose_name_plural = 'Сайдбар'