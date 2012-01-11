from spreecity.user_management.models import Member, Partner
from django.contrib import admin
 
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country', 'city', 'email',)   
    search_fields = ['first_name']
                        
class PartnerAdmin(admin.ModelAdmin):    
    list_display = ('company_name', 'company_country', 'business_name', 'business_type','business_description',)  
    list_filter = ['company_name']

admin.site.register(Member, MemberAdmin)
admin.site.register(Partner, PartnerAdmin)