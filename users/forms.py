from django import forms
from django.core.exceptions import ValidationError

from .models import UserInfo


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
