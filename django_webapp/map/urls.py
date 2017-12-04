from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),# /map/
    url(r'^(?P<campus_id>[0-9]+)/$', views.campus_show, name="campus_show"),# /map/campus
]