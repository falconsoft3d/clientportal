from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminBase

# Register your models here.

# Register your models here.
class BaseAdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_display_link = ('name', 'email', 'phone')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
admin.site.register(AdminBase, BaseAdminAdmin)
