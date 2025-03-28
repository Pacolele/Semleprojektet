from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from .models import Semlor, Rating
from ipware import get_client_ip


def index(request):
    semlor = Semlor.objects.annotate(
        _annotated_avg=Avg('ratings__rating')
    ).filter(_annotated_avg__isnull=False).order_by('-_annotated_avg')[:3]
    context = {'semlor': semlor}
    return render(request, 'semlerating/index/index.html', context)


def semlor(request):
    semlor = Semlor.objects.all()
    client_ip, is_routable = get_client_ip(request)
    context = {'semlor': semlor}
    if request.headers.get('HX-Request'):
        return render(request, 'semlerating/semlor/partials/semlor_list.html', context)
    return render(request, 'semlerating/semlor/semlor.html', context)


@require_http_methods(['POST'])
def rate_semla(request, semla_id):
    semla = get_object_or_404(Semlor, pk=semla_id)
    rating = request.POST.get('rating')
    comment = request.POST.get('comment', '')
    Rating.objects.create(semla=semla, rating=int(rating), comment=comment)
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'ratingUpdated'
    return response


def rate_form(request, semla_id):
    semla = get_object_or_404(Semlor, pk=semla_id)
    context = {'semla': semla}
    return render(request, 'semlerating/form/rate_form.html', context)
