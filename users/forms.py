from .models import UserInfo
import re

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from users.models import User


class UserInfoForm(forms.ModelForm):
    """
    Модель для создания авто полей в html для отладки пока нет фронта
    """
    class Meta:
        model = UserInfo
        fields = ['last_name', 'first_name', 'surname', 'birth_date', 'phone_number', 'img']

    def update_field_attributes(self):
        """
        Метод для авто обработки форм в цикле (вместо миксин)
        """
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Введите {self.fields[field_name].label.lower()}'
            })

    def clean_img(self):
        """
        Ограничения на загружаемую картинку, объем не больше 5 мб, формат .jpeg, .jpg и .png
        """
        img = self.cleaned_data.get('img')
        if img:
            img_name = img.name.lower()
            if not (img_name.endswith('.jpeg') or img_name.endswith('.png') or img_name.endswith('.jpg')):
                raise ValidationError('Выберите изображение в формате .jpeg, .jpg или .png')
            max_size = 5 * 1024 * 1024
            if img.size > max_size:
                raise ValidationError('Максимальный вес загружаемого изображения не должен превышать 5 Мб ')
            return img

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
