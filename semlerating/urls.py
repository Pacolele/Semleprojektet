from django.urls import path

from . import views

app_name = 'semlerating'
urlpatterns = [
    path("", views.index, name="index"),
    path("semlor/", views.semlor, name="semlor"),
    path("semlor/rate/<int:semla_id>",
         views.rate_semla, name="rate_semla"),
    path("semlor/rate-form/<int:semla_id>/",
         views.rate_form, name="rate_form"),
]
