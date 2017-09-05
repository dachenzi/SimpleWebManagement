from django.shortcuts import render,HttpResponse,redirect
from HostManager.models import  Host,Serviceline
from UserLogin.models import UserInfo
import json
# Create your views here.

def auth(func):
    def wapper(request,*args,**kwargs):
        if request.COOKIES.get('helloworld'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/user/login/')
    return wapper

@auth
def index(request):

    return render(request,'index.html')

@auth
def host(request):

    host_list = Host.objects.all()

    user_list = UserInfo.objects.all()

    service_list = Serviceline.objects.all()

    return render(request,'host.html',locals())

@auth
def addhost(request):

    ret_code = {'status':True,'error':False}

    if request.method == 'POST':

        hostname = request.POST.get('hostname')

        ipaddr = request.POST.get('ipaddr')

        serviceline = request.POST.get('serviceline')

        admin_list = request.POST.getlist('admin')

        host_obj = Host.objects.create(hostname=hostname,ipaddr=ipaddr,services_line_id=serviceline)

        host_obj.admin.add(*admin_list)

        return HttpResponse(json.dumps(ret_code))
