from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VideoForm, UserProfileForm
from .models import Video


# Create your views here.
@login_required(login_url='index')
def index(request):
    return render(request, 'matrix-admin/index2.html')


@login_required(login_url='index')
def display_video(request, video_id=None):
    if video_id:
        try:
            current_video = Video.objects.get(id=video_id)
            next_video = Video.objects.filter(id__gt=current_video.id).order_by('id').first()
            previous_video = Video.objects.filter(id__lt=current_video.id).order_by('-id').first()
        except Video.DoesNotExist:
            current_video = None
            next_video = None
            previous_video = None
    else:
        current_video = Video.objects.first()
        next_video = Video.objects.exclude(id=current_video.id).order_by('id').first()
        previous_video = Video.objects.filter(id__lt=current_video.id).order_by('-id').first()

    return render(request, 'matrix-admin/All_Videos_Page.html',
                  {'video': current_video, 'next_video': next_video, 'previous_video': previous_video})






@login_required(login_url='index')
def UploadVideo(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user.userprofile
            video.save()
            return redirect('landing_index')
    else:
        form = VideoForm()
    return render(request, 'matrix-admin/Upload_Video.html', {'form': form})

@login_required(login_url='index')
def UpdateVideo(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            video = form.save()
            return redirect('admin_all_videos')
    else:
        form = VideoForm(instance=video)
    return render(request, 'matrix-admin/updateVideo.html', {'form': form, 'video': video})


@login_required(login_url='index')
def DeleteVideo(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('admin_all_videos')
    return render(request, 'matrix-admin/All_Videos_Page.html', {'video': video})




@login_required(login_url='index')
def usersProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('landing_index')
    else:
        form = UserProfileForm()
    return render(request, 'userProfile.html', {'form': form})

@login_required(login_url='index')
def usersDashboard(request):
    return render(request, 'matrix-admin/index2.html')

@login_required(login_url='index')
def DataTable(request):
    video = Video.objects.all()
    return render(request, 'matrix-admin/tables.html', {'video': video})