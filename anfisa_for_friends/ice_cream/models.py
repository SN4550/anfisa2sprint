from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Название категории')
    slug = models.SlugField(
        'Слаг',
        max_length=64,
        unique=True)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения',
        default=100)

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'  # расширенное имя модели, можно для админки
        verbose_name_plural = 'Категории'  # только во множественном числе

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256)
    slug = models.SlugField(
        'Слаг',
        max_length=64,
        unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Топинг'
        verbose_name_plural = 'Топинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        ordering = ['title']
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Упаковки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256)
    description = models.TextField(
        'Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        verbose_name='Упаковка',
        related_name='ice_cream',
        null=True,
        blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='ice_creams')
    toppings = models.ManyToManyField(
        Topping,
        related_name='Топинги')
    is_on_main = models.BooleanField(
        'На главную',
        default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'

    def __str__(self):
        return self.title
