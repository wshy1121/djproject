from django.conf.urls import patterns, include, url

from django.contrib import admin
from jobs.views import hello, homepage, ctime, template, current_datetime, current_datetime1
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^$', homepage),
    url(r'^ctime/(\d{1,2})/$', ctime),
    url(r'^template/$', template),
    url(r'^current_datetime/$', current_datetime),
    url(r'^current_datetime1/$', current_datetime1),
)


