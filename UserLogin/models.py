from django.db import models


# Create your models here.


class UserInfo(models.Model):
    '''
    用户信息表
    '''
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    role = models.CharField(max_length=32)
    dep = models.ForeignKey('Department')


class Department(models.Model):
    '''
    部门表
    '''
    did = models.AutoField(primary_key=True)
    depname = models.CharField(max_length=32)