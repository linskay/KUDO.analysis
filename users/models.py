from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.db import models


class CustomUserManager(UserManager):
	""" Кастомный менеджер модели пользователя,
	где адрес электронной почты является уникальным идентификатором для аутентификации.
	"""

	def create_user(self, email, password=None, **extra_fields):
		""" Создание и сохранение пользователя с указанной почтой и паролем. """
		if not email:
			raise ValueError('Поле с электронной почтой должен быть заполнено!')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		# Присваиваем пользователю группу User
		user_group = Group.objects.get(name="User")
		user.groups.add(user_group)

		return user

	def create_superuser(self, email, password=None, **extra_fields):
		""" Создание и сохранение супер пользователя с указанной почтой и паролем. """
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser должен иметь флажок is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser должен иметь флажок is_superuser=True.')

		return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
	""" Создание пользователя """
	username = None
	email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите email")
	token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)
	is_token_used = models.BooleanField(default=False, verbose_name="Токен использован")

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"

	def __str__(self):
		return self.email