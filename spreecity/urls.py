from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spreecity.views.home', name='home'),
    # url(r'^spreecity/', include('spreecity.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^user_management/',include('spreecity.user_management.urls')),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',                        
                {'document_root': settings.STATIC_DOC_ROOT}),
                       
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/admin'}),

)
