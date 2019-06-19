from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, nmae = 'index'),
    path('new/', views.new, name = 'new'),
    path('detail/', views.detail, name = 'detail'),
]