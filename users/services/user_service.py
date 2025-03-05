import secrets

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect

# from config.settings import EMAIL_HOST_USER
from users.models import User, UserInfo


class UserService:
	@staticmethod
	def create_user(form):
		"""Создает пользователя, ставит флажок is_active который по дефолту True в False,
		генерирует токен, ставит флажок is_token_used = False
		добавляет пользователя его в группу "User" и создает связанный класс UserInfo."""
		user = form.save()
		user.is_active = False
		user.token = secrets.token_hex(16)
		user.is_token_used = False
		user.save()

		# Добавление пользователя в группу "User"
		user_group = Group.objects.get(name="User")
		user.groups.add(user_group)

		# Создаем связанную таблицу UserInfo
		UserInfo.objects.create(user=user, email=user.email)

		return user

	@staticmethod
	def generate_confirmation_url(request, token):
		""" Создает URL для подтверждения email. """
		host = request.get_host()
		return f"http://{host}/users/email-confirm/{token}/"

	@staticmethod
	def send_confirmation_email(user, url):
		""" Отправляет email для подтверждения и установления флажков is_active=True,
		is_token_used=True в случае перехода по ссылке"""
		send_mail(
			subject="Подтверждение почты",
			message=f"Переход по ссылке для подтверждения почты {url}",
			from_email=EMAIL_HOST_USER,
			recipient_list=[user.email],
		)
		print(f"Ссылка для подтверждения почты отправлена на: {user.email}")

	@staticmethod
	def send_to_console_confirmation_email(user, url):
		""" Отправляет email для подтверждения через консольный бэкенд. """
		send_mail(
			subject="Подтверждение почты",
			message=f"Переход по ссылке для подтверждения почты: {url}",
			from_email=settings.DEFAULT_FROM_EMAIL,
			recipient_list=[user.email],
		)

	@staticmethod
	def email_verification_service(token):
		"""Подтверждение email пользователя по токену"""
		user = get_object_or_404(User, token=token)

		if user.is_token_used:
			return {"status": "error", "message": "Ссылка уже была использована"}

		if user.is_active:
			return {"status": "warning", "message": "Ваш аккаунт уже активирован"}

		user.is_active = True
		user.is_token_used = True
		user.save()

		return {"status": "success", "message": "Ваш аккаунт успешно активирован!"}
