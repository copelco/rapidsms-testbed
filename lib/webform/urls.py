from django.conf.urls.defaults import *
from webform import views

urlpatterns = patterns('',
    url(r'^send/$', views.send_message, name='send-message'),
)
