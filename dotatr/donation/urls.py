from django.conf.urls import patterns, url

from donation import views

urlpatterns = patterns('',
    url(r'^$', views.donate_page, name='donate_page')
    url(r'^success/$', views.donate_page_success, name='donate_page_success')
)