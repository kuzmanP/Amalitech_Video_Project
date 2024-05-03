from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'matrix-admin/index2.html')

def usersDashboard(request):
    return render(request,'matrix-admin/index.html')