#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

import player.regbackend 
from registration.backends.default.views import RegistrationView
from player.forms import PlayerRegForm



from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.decorators import login_required

from social_auth.views import auth, complete, disconnect



urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name='index'),
    url(r'^nodetest/$', 'nodetest.views.test', name='test'),
    url(r'^nodetest/tooltip/(?P<id>[^/]+)/$', 'nodetest.views.tooltip'),


    # Examples:
    # url(r'^$', 'dotatr.views.home', name='home'),
    # url(r'^dotatr/', include('dotatr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', 
        include(admin.site.urls)),
    url(r'^haberler/', 
        include('news.urls'),
        name='haberler'),
    ('^activity/', include('actstream.urls')),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=PlayerRegForm)), 
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += patterns('',
    url(r'^associate/(?P<backend>[^/]+)/$',
        login_required(auth),
        name='socialauth_begin'),
    url(r'^associate/complete/(?P<backend>[^/]+)/$',
        login_required(complete),
        name='socialauth_complete'),

    url(r'^disconnect/(?P<backend>[^/]+)/$',
        disconnect,
        name='socialauth_disconnect'),
    url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>[^/]+)/$',
        disconnect,
        name='socialauth_disconnect_individual'),
)
