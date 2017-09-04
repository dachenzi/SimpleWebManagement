from django.db import models
from UserLogin.models import UserInfo

# Create your models here.


class Host(models.Model):

    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    ipaddr = models.GenericIPAddressField()
    admin = models.ManyToManyField(UserInfo)
    services_line = models.ForeignKey('Serviceline')


class Serviceline(models.Model):

    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=32)

