from django.urls import path

from .import views

from .views import index,usersDashboard

urlpatterns=[
    path('', views.index, name='index'),
    path('userDashboard', views.usersDashboard, name='user_dashboard'),
]