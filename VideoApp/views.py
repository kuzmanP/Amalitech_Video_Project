from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'matrix-admin/index2.html')

def All_Videos(request):
    return render(request,'matrix-admin/All_Videos_Page.html')

def UploadVideo(request):
    return render(request,'matrix-admin/Upload_Video.html')

def usersDashboard(request):
    return render(request,'matrix-admin/index.html')