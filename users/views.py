from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView

from .forms import UserInfoForm
from .models import UserInfo


class UserInfoDeleteView(DeleteView):
    model = UserInfo
    template_name = 'users/confirm_delete.html'
    success_url = reverse_lazy('user_detail')

    def get_success_url(self):
        return reverse_lazy('users:user_detail', kwargs={'pk': self.object.pk})


class UserInfoUpdateView(UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_detail')

    def get_success_url(self):
        return reverse_lazy('users:user_detail', kwargs={'pk': self.object.pk})


class UserInfoDetailView(DetailView):
    model = UserInfo
    template_name = 'user_detail.html'
    success_url = reverse_lazy('user_detail')

    def get_success_url(self):
        return reverse_lazy('users:user_detail', kwargs={'pk': self.object.pk})

