from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'userID', 'email', 'birth', 'belong', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'userID', 'birth', 'belong',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'birth', 'userID', 'belong', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'name', 'belong',)
    ordering = ('email', 'birth', 'name', )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)