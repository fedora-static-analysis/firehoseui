from django.conf.urls import patterns

from firehoseui import views

urlpatterns = patterns('',
   (r'^reports/$', views.reports),
   (r'^upload_file/$', views.upload_file),
)
