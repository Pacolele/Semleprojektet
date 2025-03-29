from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
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
    context = {'semlor': semlor}
    print(request.headers)
    if request.headers.get('HX-Request'):
        return render(request, 'semlerating/semlor/partials/semlor_list.html', context)
    return render(request, 'semlerating/semlor/semlor.html', context)


@require_http_methods(['POST'])
def rate_semla(request, semla_id):
    semla = get_object_or_404(Semlor, pk=semla_id)
    rating = request.POST.get('rating')
    comment = request.POST.get('comment', '')

    client_ip, is_routable = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]

    cutoff_time = timezone.now() - timedelta(hours=24)
    recent_reviews = Rating.objects.filter(
        ip_address=client_ip,
        user_agent=user_agent,
        created_at__gte=cutoff_time
    ).count()

    if recent_reviews >= 5:
        return JsonResponse({'error': 'You have reached the limit of 5 ratings per 24 hours'})

    Rating.objects.create(semla=semla, rating=int(
        rating), comment=comment, ip_address=client_ip, user_agent=user_agent)
    return HttpResponse(
        status=200,
        headers={"HX-Trigger": "ratingUpdated"}
    )


def rate_form(request, semla_id):
    semla = get_object_or_404(Semlor, pk=semla_id)
    context = {'semla': semla}
    return render(request, 'semlerating/form/rate_form.html', context)
