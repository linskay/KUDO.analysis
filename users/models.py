from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UserInfo(models.Model):
    """
    Модель для странички в личном кабинете
    """
    id = models.AutoField(primary_key=True, verbose_name='id')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    surname = models.CharField(max_length=30, verbose_name='Отчество')
    email = models.EmailField(null=True, verbose_name='Адрес почты')
    registration_date = models.DateField(verbose_name='Дата регистрации')
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    img = models.ImageField(upload_to='media/img/', default='404 error', verbose_name='Изображение')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']

