from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'alnourish.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^home/', include('vs.urls',namespace='home')),
    url(r'^admin/', include(admin.site.urls)),
]
