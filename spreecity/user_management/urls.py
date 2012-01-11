from django.conf.urls.defaults import *

urlpatterns = patterns('spreecity.user_management.views',
    (r'^member_creation/', 'member_creation'),  
    (r'^partner_creation/', 'partner_creation'), 
 
)
