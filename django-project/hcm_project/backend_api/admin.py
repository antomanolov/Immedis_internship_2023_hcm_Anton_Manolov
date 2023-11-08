from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from hcm_project.backend_api.appuser import AppUser
from hcm_project.backend_api.models.app_models import Attendance, LeaveBallance, LeaveRequest, Payroll, PerformanceReview, Task
from hcm_project.backend_api.models.custom_user_model import Department, JobTitle


class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser


class CustomAdmin(UserAdmin):
    form = CustomChangeForm
    fieldsets = (
        ('User Personal Information', {'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'telephone_number',)}),
        ('Work details', {'fields': ('location', 'department', 'job_title', 'seniority', 'is_hr')}),
        ('Important dates', {'fields': ('last_login', 'date_of_hire', 'date_of_dismiss')}),
        ('Eligible for payment', {'fields': ('is_eligible_for_payment', )}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),  # Move permission fields to this section
    )

    list_display = ('email', 'first_name', 'last_name', 'department', 'job_title', 'seniority')
    
    ordering = ('department',)

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name","last_name","password1", "password2", 'is_hr'),
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('date_joined', 'last_login', 'email',  'last_profile_edit', 'date_of_hire')
        return ()


class LeaveBalanceAdmin(admin.ModelAdmin):
    readonly_fields = ('employee',)
# Custom User admin panel
admin.site.register(AppUser, CustomAdmin)

# All other models in admin panel
admin.site.register(Department)
admin.site.register(JobTitle)
admin.site.register(Payroll)
admin.site.register(LeaveBallance, LeaveBalanceAdmin)
admin.site.register(LeaveRequest)
admin.site.register(Attendance)
admin.site.register(PerformanceReview)
admin.site.register(Task)
