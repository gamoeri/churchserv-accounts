from django.conf.urls import patterns, include, url
from accounts.views import hello, index, current_datetime, home
from auth.views import log_in, register, log_out
from snippets.views import snippets
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^hello/$', hello),
	url(r'^$', index),
	url(r'^time/$', current_datetime),
  url(r'^login/$', log_in),
  url(r'^register/$', register),
  url(r'^home/$', home),
  url(r'^logout/$', log_out),
  url(r'^snippets/$', snippets),
    # Examples:
    # url(r'^$', 'accounts.views.home', name='home'),
    # url(r'^accounts/', include('accounts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
