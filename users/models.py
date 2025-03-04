from django.contrib.auth.models import AbstractUser, Group, UserManager
from django.db import models


class CustomUserManager(UserManager):
    """Кастомный менеджер модели пользователя,
    где адрес электронной почты является уникальным идентификатором для аутентификации.
    """

    def create_user(self, email, password=None, **extra_fields):
        """Создание и сохранение пользователя с указанной почтой и паролем."""
        if not email:
            raise ValueError("Поле с электронной почтой должен быть заполнено!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # Присваиваем пользователю группу User
        user_group = Group.objects.get(name="User")
        user.groups.add(user_group)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Создание и сохранение супер пользователя с указанной почтой и паролем."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser должен иметь флажок is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser должен иметь флажок is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ Модель для создания и управления пользователями в базе данных через ORM.
    Использует email в качестве уникального идентификатора вместо username.
    """

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите email"
    )
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )
    is_token_used = models.BooleanField(default=False, verbose_name="Статус использования токена")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class UserInfo(models.Model):
    """
    Модель для странички в личном кабинете
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    surname = models.CharField(max_length=30, verbose_name="Отчество")
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите email")
    registration_date = models.DateField(verbose_name="Дата регистрации")
    birth_date = models.DateField(verbose_name="Дата рождения")
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Номер телефона"
    )
    img = models.ImageField(
        upload_to="media/img/", default="404 error", verbose_name="Изображение"
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

