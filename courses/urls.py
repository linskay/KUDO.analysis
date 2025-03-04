from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib import admin
from django.urls import path


from users.apps import UsersConfig
from courses import views
from users.views import UserRegisterView

app_name = 'courses'

urlpatterns = [
	path("", views.CoursesListView.as_view(), name="courses"),
    path("all", views.CoursesListAllView.as_view(), name="courses_all"),
    path("complete", views.CoursesListCompleteView.as_view(), name="courses_complete"),
	path("<int:pk>", views.CoursesDetailView.as_view(), name="courses_detail"),
    path("create", views.CoursesCreateView.as_view(), name="courses_create"),
    path("<int:pk>/update", views.CoursesUpdateView.as_view(), name="courses_update"),
    path("<int:pk>/delete", views.CoursesDeleteView.as_view(), name="courses_delete"),
]


#/mylearn
#mylearn.complete
#learn.all