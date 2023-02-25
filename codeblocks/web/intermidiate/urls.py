from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.shorten, name='shorten_post'),
    path('<str:short_id>', views.redirect_to_url, name='shorten'),
]