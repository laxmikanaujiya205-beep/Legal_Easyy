from django.contrib import admin
from .models import Contact,Feedback,User,LegalAdvisor,FirmService
# Register your models here.
class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","phone","query","date"]






admin.site.register(Contact,Contact_Admin)
class Feedback_Admin(admin.ModelAdmin):
    list_display=["name","email","rating","remarks"]

admin.site.register(Feedback,Feedback_Admin)
admin.site.register(User)
admin.site.register(LegalAdvisor)
admin.site.register(FirmService)

admin.site_header="Legal Firm Admin Dashboard"

admin.site.site_title="Justice is your Right"
admin.site.index_title="Law Solutions Plateform"


