from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
)

urlpatterns += patterns('books.views',
    url(r'^search/$', 'search'),
    url(r'^contact/$', 'contact'),
    url(r'^add_publisher/$', 'add_publisher'),
)

urlpatterns += patterns('jobs.views',
    url(r'^hello/$', 'hello'),
    
    url(r'^ctime/(\d{1,2})/$', 'ctime'),
    url(r'^template/$', 'template'),
    url(r'^current_datetime/$', 'current_datetime'),
    url(r'^current_datetime1/$', 'current_datetime1'),

)
