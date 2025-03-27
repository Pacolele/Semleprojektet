from django.shortcuts import render
from django.db.models import Avg
from django.template import loader
from django.http import HttpResponse
from .models import Semlor


def index(request):
    semlor = Semlor.objects.annotate(
        avg_rating=Avg('ratings__rating')).order_by('-avg_rating')[:3]
    template = loader.get_template("semlerating/index.html")
    context = {'semlor': semlor}
    return HttpResponse(template.render(context, request))


def semlor(request):
    semlor = Semlor.objects.all()
    template = loader.get_template("semlerating/index.html")
    context = {'semlor': semlor}
    return HttpResponse(template.render(context, request))
