from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import RequestContext, loader

from brend.models import Brend


def brend(request, brend_id):
    obj = Brend.objects.get(pk=brend_id)
    template = render(request, 'brend.html',
                      context={'title': obj.name, 'id': brend_id, 'code': obj.code})
    return template


def brends(request):
    data = Brend.objects.order_by('id')
    template = loader.get_template('brends.html')
    context = {
        'data': data,
        'title': 'Фирмы-производители',
    }
    return HttpResponse(template.render(context))
