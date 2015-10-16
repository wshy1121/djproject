from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('books.views',
    url(r'^search/$', 'search'),
    url(r'^contact/$', 'contact'),
    url(r'^add_publisher/$', 'add_publisher'),
)

urlpatterns += patterns('jobs.views',
    url(r'^hello/$', 'hello', {'template_name': 'template1.html'}),
    url(r'^ctime/(\d{1,2})/$', 'ctime'),
    url(r'^template/$', 'template'),
    url(r'^current_datetime/$', 'current_datetime'),
    url(r'^current_datetime1/$', 'current_datetime1'),

)

from jobs.views import MyView
urlpatterns += patterns('jobs.views',
	url(r'^about/$', TemplateView.as_view(template_name='base.html')),
	url(r'^about/(\w+)/$', 'about_pages'),
	url(r'^mine/$', MyView.as_view(), name='my-view'),
)

if settings.DEBUG:
	urlpatterns += patterns('jobs.views',
		url(r'^$', 'homepage'),
	)

