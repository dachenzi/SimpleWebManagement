
from django.conf.urls import url,include
from UserLogin import views


urlpatterns = [
    url(r'^login',views.login),
    url(r'^logout',views.logout),
]
