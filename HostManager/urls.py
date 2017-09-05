from django.conf.urls import url,include
from HostManager import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^host/', views.host),
    url(r'^addhost/', views.addhost),
]
