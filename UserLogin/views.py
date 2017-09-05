from django.shortcuts import render,HttpResponse,redirect
from utils import encrypt
from UserLogin import models

# Create your views here.

def login(request):

    '''
    用户登陆
    :param request:  用户登陆请求的所有信息
    :return:    返回登陆页面
    '''

    if request.method == 'GET':

        return render(request,'login.html')

    else:

        username = request.POST.get('username')
        password = request.POST.get('password')
        password = encrypt.encrypt(password)

        user_obj = models.UserInfo.objects.filter(username=username,password=password).first()

        if user_obj:

            response = redirect('/manage/index/')
            response.set_cookie('helloworld',username)

            return response
        else:

            return render(request,'login.html',{'msg':'用户名或密码不正确'})

def logout(request):

    response = redirect('/user/login/')
    response.delete_cookie('helloworld')

    return response