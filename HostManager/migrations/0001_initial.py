# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserLogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=32)),
                ('ipaddr', models.GenericIPAddressField()),
                ('admin', models.ManyToManyField(to='UserLogin.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Serviceline',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='services_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostManager.Serviceline'),
        ),
    ]