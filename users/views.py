import secrets

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from users.forms import UserRegisterForm, UserInfoForm
from users.models import User, UserInfo
from users.services.user_service import UserService


class UserRegisterView(CreateView):
    """Представление для регистрации нового пользователя.
        Методы:
    - form_valid: Обрабатывает данные формы, создает пользователя, генерирует токен
      для подтверждения email и отправляет ссылку для подтверждения.
    """

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        # Создаем пользователя через сервис c логикой присвоение группы "User" и создание связанного класса UserInfo
        user = UserService.create_user(form)

        # Создаем URL для подтверждения email
        url = UserService.generate_confirmation_url(self.request, user.token)

        # Отправляем email для подтверждения
        UserService.send_confirmation_email(user, url)

        return super().form_valid(form)


def email_verification(request, token):
    """Подтверждение email пользователя по токену"""
    result = UserService.email_verification_service(token)

    return render(request, "users/email_verification.html", {"message": result["message"]})


class UserInfoUpdateView(UpdateView):
    """
    Класс контроллер для добавления информации в пустое (редактировании уже созданной инфы) о пользователе
    """

    model = UserInfo
    form_class = UserInfoForm
    template_name = "users/update.html"
    success_url = reverse_lazy("user_detail")

    def get_success_url(self):
        return reverse_lazy("users:user_detail", kwargs={"pk": self.object.pk})


class UserInfoDetailView(DetailView):
    """
    Класс контроллер для отображения странички с информацией о пользователе
    """

    model = UserInfo
    template_name = "users/user_detail.html"
    success_url = reverse_lazy("user_detail")

    def get_success_url(self):
        return reverse_lazy("users:user_detail", kwargs={"pk": self.object.pk})


class UserInfoDeleteView(DeleteView):
    """
    Класс контроллер для удаления всей информации о пользователе из лк (пока всей)
    """

    model = UserInfo
    template_name = "users/confirm_delete.html"
    success_url = reverse_lazy("user_detail")

    def get_success_url(self):
        return reverse_lazy("users:user_detail", kwargs={"pk": self.object.pk})
