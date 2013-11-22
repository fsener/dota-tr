from django.conf.urls import patterns, url

from donation import views

urlpatterns = patterns('',
    url(r'^$', views.donate_page, name='donate_page')
)