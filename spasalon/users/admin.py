from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "is_staff",
    )
    readonly_fields = (
        "email",
        "username",
    )
    fieldsets = (
        (
            "данные идентификации",
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                )
            },
        ),
        (
            "другие данные пользователя",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "разрешения",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )


site.register(CustomUser, CustomUserAdmin)
