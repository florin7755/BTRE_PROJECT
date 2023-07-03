from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    
    
admin.site.register(Contact, ContactAdmin)    