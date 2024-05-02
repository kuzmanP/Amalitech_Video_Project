from django.urls import path

from .import views

from .views import index,register

urlpatterns=[
    path('login', views.index, name='index'),
    path('register', views.register, name='register'),
]