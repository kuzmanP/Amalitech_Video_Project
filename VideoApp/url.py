from django.urls import path

from .import views

from .views import index,usersDashboard,display_video,UploadVideo,usersProfile,UpdateVideo,DataTable,DeleteVideo
urlpatterns=[
    path('', views.index, name='landing_index'),
    path('userDashboard', views.usersDashboard, name='user_dashboard'),
    path('table_view', views.DataTable, name='table_data'),
    path('userProfile', views.usersProfile, name='user_profile'),
    path('admin/all_videos/', views.display_video, name='admin_all_videos'),
    path('admin/all_videos/<uuid:video_id>', views.display_video, name='next_video'),
    path('admin/upload_video', views.UploadVideo, name='admin_upload_video'),
    path('admin/update_video/<uuid:video_id>', views.UpdateVideo, name='admin_update_video'),
    path('admin/delete_video/<uuid:video_id>', views.DeleteVideo, name='admin_delete_video'),
]