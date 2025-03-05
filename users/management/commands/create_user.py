from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Создает нового пользователя"

    def handle(self, *args, **kwargs):
        email = input("Введите email пользователя: ")
        password = input("Введите пароль пользователя: ")

        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f"Пользователь с email {email} уже существует!")
            )
            return

        user = User.objects.create_user(email=email, password=password)

        self.stdout.write(self.style.SUCCESS(f"Пользователь {email} создан!"))
