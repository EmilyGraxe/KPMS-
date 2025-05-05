from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        (_('Personal info'), {'fields': ()}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'role', 'branch', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'password1', 'password2', 'role','groups', 'user_permissions'),
        }),
    )
    list_display = ('user_id', 'role', 'is_admin', 'is_active')
    search_fields = ('user_id',)
    ordering = ('user_id',)
    list_filter = ('is_admin', 'is_active')
    filter_horizontal = ("groups", "user_permissions")

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Group)



# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'role', 'is_staff')
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('role',)}),
#     )
# admin.site.register(CustomUser, CustomUserAdmin)  # Register the custom user model with the admin site