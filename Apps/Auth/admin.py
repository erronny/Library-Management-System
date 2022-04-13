from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreateForm, UserEditForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add change user instance
    form = UserEditForm
    add_form = UserCreateForm

    """ 
     The fields to be used in displaying the user model. These override the definitions on the base 
     UserAdmin that reference specific fields on auth.User .
     """
    list_display = ['email', 'is_superuser']
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    """ 
    add_fieldsets is not a standard ModelAdmin attribute. UserAdmin override get_fieldsets to use this
    attribute when creating a user.
    """

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password')
        }),
    )

    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

# Add Group model from admin. If you want to use it later
# admin.site.register(Group)
