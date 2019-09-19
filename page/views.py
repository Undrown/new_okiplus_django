from django.shortcuts import render

# Create your views here.
from page.models import Page


def page(request, page_name):
    obj = Page.objects.get(name=page_name)
    return render(request, 'page.html', context={'name': obj.name, 'code': obj.code, 'title': obj.title, })


def index(request):
    obj = Page.objects.get(name='index')
    return render(request, 'page.html', context={'name': 'index', 'code': obj.code, 'title': obj.title, })
