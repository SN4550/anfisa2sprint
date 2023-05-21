from django.shortcuts import render, get_object_or_404

from .models import IceCream


def ice_cream_detail(request, pk):
    # можно и квери сет сунуть чтобы получить выборку
    ice_cream = get_object_or_404(
        IceCream.objects.values(
            'title', 'description').filter(is_published=True), pk=pk)

    template = 'ice_cream/detail.html'
    context = {'ice_cream': ice_cream}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
