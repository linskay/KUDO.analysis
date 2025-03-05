from django.contrib import admin

from users.models import User, UserInfo


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация для отображения пользователя в админ панели."""

    list_display = (
        "id",
        "email",
    )
    list_filter = ("is_active",)
    search_fields = ("email",)


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):

    list_display = ("user", "email", "last_name", "birth_date", "phone_number",)
    list_filter = ("email", "last_name", "registration_date",)
    search_fields = ("email", "last_name",)
