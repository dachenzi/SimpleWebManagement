from django.shortcuts import render,HttpResponse,redirect
from HostManager.models import  Host,Serviceline
from UserLogin.models import UserInfo

# Create your views here.

def index(request):

    return render(request,'index.html')


def host(request):

    host_list = Host.objects.all()

    user_list = UserInfo.objects.all()

    service_list = Serviceline.objects.all()

    return render(request,'host.html',locals())