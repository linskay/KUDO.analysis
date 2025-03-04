from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.forms import CustomLoginForm
from users.views import UserRegisterView

from .views import UserInfoDeleteView, UserInfoDetailView, UserInfoUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="users/login.html", form_class=CustomLoginForm),
        name="login",
    ),
    path("logout/", LogoutView.as_view(template_name="home.html"), name="logout"),
    path("user_detail/<int:pk>/", UserInfoDetailView.as_view(), name="user_detail"),
    path("user/<int:pk>/edit/", UserInfoUpdateView.as_view(), name="user_edit"),
    path("user/<int:pk>/delete/", UserInfoDeleteView.as_view(), name="user_delete"),
]
