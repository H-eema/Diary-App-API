from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        "username",
        "email",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "full_name",
                    "email",
                    "username",
                    "age",
                    "occupation",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "full_name",
                    "email",
                    "username",
                    "age",
                    "occupation",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
