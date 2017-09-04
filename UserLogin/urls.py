
from django.conf.urls import url,include
from UserLogin import views


urlpatterns = [
    url(r'^$',views.login),
]
