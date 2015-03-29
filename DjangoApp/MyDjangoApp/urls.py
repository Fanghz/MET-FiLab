from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyDjangoApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'Django.views.index', name='index'),
    url(r'^home/$', 'Django.views.home', name='newHome'),
    url(r'^accounts/profile/$', 'Django.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('login')}, name='logout'),
    # (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^failedbanks/$', 'Django.views.failedbanks'),
    url(r'^search/$', 'Django.views.search'),
    url(r'^stockprice/$', 'Django.views.stockprice'),
    url(r'^test/$', 'Django.views.test'),
    url(r'register/$','Django.views.register'),
    url(r'^login/$', 'Django.views.login'),
    url(r'^sentiment/$', 'Django.views.sentiment'),
)
