from django.conf.urls import patterns, url
from jobtrak_public import views

urlpatterns = patterns('',
#    url(r'^data/(?P<test_id>\d+)/$', views.chart_data_json, name='chart_data_json'),
#    url(r'^data/$', views.chart_data_json, name='chart_data_json'),
    url(r'^$',views.index,name='index'),
)