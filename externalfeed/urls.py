from django.conf.urls import patterns, url

from externalfeed.views import Index, List, Entry

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='externalfeed-index'),
    url(r'^list/$', List.as_view(), name='externalfeed-list'),
    url(r'^(?P<path>.*)$', Entry.as_view(), name='externalfeed-entry'),
    )
