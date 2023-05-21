from django.contrib import admin

from .models import (Category, Topping,
                     Wrapper, IceCream)


# задаем дефолтное название для всех пустых значений в полях админки
admin.site.empty_value_display = 'Не  задано'


# Подготавливаем модель для вставки ее на страницу другой модели
class IceCreamInLine(admin.StackedInline):
    model = IceCream
    # если значение > 0, добавляет раскрытую форму интегрируемой модели
    # если переменной extra нет, выводится 3 формы
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # вставляем другую модель
    inlines = (IceCreamInLine,)

    list_display = ['title',
                    'slug',
                    'output_order',
                    'is_published']


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'slug',
                    'is_published']


@admin.register(Wrapper)
class WrapperAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'is_published']


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    # Какие поля выводим в админку
    list_display = ['title',
                    'description',
                    'is_published',
                    'wrapper',
                    'category',
                    'is_on_main']

    # какие из этих полей в админке можно редактировать
    list_editable = ['is_published',
                     'category',
                     'is_on_main']

    # по какому полю поиск
    search_fields = ['title']

    # по каким полям будет фильтр
    list_filter = ['category']

    # интерфейс перекидывания значений для указанных полей N:M
    filter_horizontal = ['toppings']

