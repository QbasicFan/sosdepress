from django.conf.urls import url
from . import views


urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    url(r'^contact/$', views.contact, name='contact'),
    #url(r'^service/$', views.service, name='service'),
    url(r'^', views.index, name='index'),
    ]
