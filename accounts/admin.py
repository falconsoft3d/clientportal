from asyncore import read
from django.contrib import admin
from .models import Account, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
# class UserProfileAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         return format_html('<img src="{}" width="30" style="border-radius:50;">'.format(object.profile_picture.url))   

#     thumbnail.short_description = 'Imagen de Perfil'
#     list_display = ( 'thumbnail', 'user', 'city', 'country' )
    
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile)