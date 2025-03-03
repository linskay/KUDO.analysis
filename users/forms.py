import re

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from users.models import User


class UserRegisterForm(UserCreationForm):
	""" Форма регистрации пользователя """
	username = forms.CharField(label="Username", widget=forms.PasswordInput(
		attrs={'class': "form-input", "placeholder": "fsdfsdf"}))
	password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(
		attrs={'class': "form-input", "placeholder": "Введите пароль"}))
	password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(
		attrs={'class': "form-input", "placeholder": "Повторите пароль"}))

	class Meta:
		model = User
		fields = ("email",)
		labels = {
			'email': 'Почта',
		}
		widgets = {
			'email': forms.TextInput(attrs={'class': "form-input", "placeholder": "Введите почту"})
		}

	def clean_email(self):
		email = self.cleaned_data['email']
		email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
		if not re.match(email_regex, email):
			raise ValidationError("Введен не корректное название почты!")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Данный email уже зарегистрирован!")
		return email


class CustomLoginForm(AuthenticationForm):
	""" Переопределенная форма аутентификации пользователя """
	username = forms.CharField(
		label="Почта",
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите почту'})
	)
	password = forms.CharField(
		label="Пароль",
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
	)
