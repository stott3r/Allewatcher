# -*- coding: utf-8 -*-
# django imports
from django.conf.urls import url
from django.conf.urls import patterns
# app imports
from search import views


urlpatterns = patterns('',
                       url(r'^free/$', 'search.views.free_search'),
                       url(r'^free/search_send/$', 'search.views.search_send'),
                       url(r'^confirmed/(?P<activation_key>\w+)/', 'search.views.search_confirmed'),
                       )
