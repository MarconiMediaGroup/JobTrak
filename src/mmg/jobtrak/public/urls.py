from django.conf.urls import patterns, include, url
from mmg.jobtrak.public import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
)