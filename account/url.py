from django.urls import path

from .import views

from .views import index,register,forgetPassword,logOut,password_reset_confirm,password_reset_complete

urlpatterns=[
    path('login', views.index, name='index'),
    path('register', views.register, name='register'),
    path('forgetPassword', views.forgetPassword, name='forget_password'),
    path('logout', views.logOut, name='logout'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_comfirm', views.password_reset_complete, name='password_reset_complete'),
]