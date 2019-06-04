from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hola/', views.hola),
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
    path('template_language/', views.template_language),
    path('isbirthday/', views.isbirthday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('name/', views.name),
    path('lotto2/', views.lotto2),
    path('picklotto/', views.picklotto),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),

]
