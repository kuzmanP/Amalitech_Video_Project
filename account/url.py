from django.urls import path

from .import views

from .views import index,register,forgetPassword,logOut

urlpatterns=[
    path('login', views.index, name='index'),
    path('register', views.register, name='register'),
    path('forgetPassword', views.forgetPassword, name='forget_password'),
    path('logout', views.logOut, name='logout'),
]