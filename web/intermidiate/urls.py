from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten', views.shorten, name='shorten_post'),
    path('shorten/<str:url>', views.shorten, name='shorten'),
]