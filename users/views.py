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

