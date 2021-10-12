from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        'email', 'first_name', 'last_name', 'gender', 'phone_number', 'is_active', 'is_admin',)
    list_filter = ('email', 'is_admin', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'gender', 'phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_admin',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    # overriding filter horizontal
    filter_horizontal = ()


# register the model and it's model admin to django admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
