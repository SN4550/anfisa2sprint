from django.shortcuts import render
from django.db.models import Q

from ice_cream.models import IceCream, Category

POST_LIMIT = 10
POST_OFFSET = 0  # [POST_OFFSET:POST_LIMIT]


def index(request):
    ice_cream_list = IceCream.objects.select_related(
        'category').filter(category__is_published=True)
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'description', 'category__title')
    # ice_cream_list = IceCream.objects.all()[:2]
    # .select_related('ice_creams')

    context = {'ice_cream_list': ice_cream_list}
    template = 'homepage/index.html'
    return render(request, template, context)
