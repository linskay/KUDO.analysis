from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация для отображения пользователя в админ панели."""

    list_display = (
        "id",
        "email",
    )
    list_filter = ("is_active",)
    search_fields = ("email",)
