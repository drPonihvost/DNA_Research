from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, UserCreationForm, UserChangeForm

from .models import User, Profile, Department


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Permissions',
            {
                'fields': (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                )
            }
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups')
            },
        ),
    )
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Department)
