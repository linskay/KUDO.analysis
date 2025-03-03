from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView

from .forms import UserInfoForm
from .models import UserInfo


class UserInfoDeleteView(DeleteView):
    """
    Класс контроллер для удаления всей информации о пользователе из лк (пока всей)
    """
    model = UserInfo
    template_name = 'users/confirm_delete.html'
    success_url = reverse_lazy('user_detail')

    def get_success_url(self):
        return reverse_lazy('users:user_detail', kwargs={'pk': self.object.pk})


class UserInfoUpdateView(UpdateView):
    """
    Класс контроллер для добавления информации в пустое (редактировании уже созданной инфы) о пользователе
    """
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_detail')

    def get_success_url(self):
        return reverse_lazy('users:user_detail', kwargs={'pk': self.object.pk})


class UserInfoDetailView(DetailView):
    """
    класс контроллер для отображения странички с информацией о пользователе
    """
    model = UserInfo
    template_name = 'users/user_detail.html'
    success_url = reverse_lazy('user_detail')

    def get_success_url(self):
        return reverse_lazy('users:user_detail', kwargs={'pk': self.object.pk})

import secrets

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class UserRegisterView(CreateView):
    """ Представление для регистрации нового пользователя.
        Методы:
    - form_valid: Обрабатывает данные формы, создает пользователя, генерирует токен
      для подтверждения email и отправляет ссылку для подтверждения.
    """
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.is_token_used = False
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        print(f"Ссылка для подтверждения почты: {url}")
        # send_mail(
        #     subject="Подтверждение почты",
        #     message=f"Переход по ссылке для подтверждения почты {url}",
        #     from_email=EMAIL_HOST_USER,
        #     recipient_list=[user.email],
        # )

        return super().form_valid(form)


def email_verification(request, token):
    """ Подтверждение email пользователя по токену """
    user = get_object_or_404(User, token=token)

    if user.is_token_used:
        messages.error(request, "Ссылка уже была использована")
        return redirect(reverse("users:login"))

    if user.is_active:
        messages.warning(request, "Ваш аккаунт уже активирован")
        return redirect(reverse("users:login"))

    user.is_active = True
    user.is_token_used = True
    user.save()

    return redirect(reverse("users:login"))

