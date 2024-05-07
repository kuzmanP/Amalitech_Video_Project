from django.urls import path

from .import views

from .views import index,usersDashboard,All_Videos,UploadVideo

urlpatterns=[
    path('', views.index, name='landing_index'),
    path('userDashboard', views.usersDashboard, name='user_dashboard'),
    path('/admin/all_videos', views.All_Videos, name='admin_all_videos'),
    path('/admin/upload_video', views.UploadVideo, name='admin_upload_video'),
]