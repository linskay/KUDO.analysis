from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.forms import CustomLoginForm
from users.views import UserRegisterView

app_name = UsersConfig.name

urlpatterns = [
	path("register/", UserRegisterView.as_view(), name="register"),
	path("login/", LoginView.as_view(template_name="login.html", form_class=CustomLoginForm), name="login"),
	path("logout/", LogoutView.as_view(template_name="home.html"), name="logout"),
]
