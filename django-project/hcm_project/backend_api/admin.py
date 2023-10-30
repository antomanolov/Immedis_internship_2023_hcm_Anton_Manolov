from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from hcm_project.backend_api.appuser import AppUser

#TODO add the rest of the fields 

class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser


class CustomAdmin(UserAdmin):
    form = CustomChangeForm
    fieldsets = (
        ('User Info', {'fields': ('first_name', 'last_name', 'date_of_birth',)}),
        ('Important dates', {'fields': ('last_login', )}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),  # Move permission fields to this section
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('date_joined', 'last_login', 'email',  'last_profile_edit', 'date_of_hire')
        return ()


admin.site.register(AppUser, CustomAdmin)
