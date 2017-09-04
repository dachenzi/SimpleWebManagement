from django.shortcuts import render,HttpResponse,redirect
from HostManager import models

# Create your views here.

def index(request):

    return render(request,'index.html')


def host(request):

    host_list = models.Host.objects.all()

    return render(request,'host.html',{'host_list':host_list})