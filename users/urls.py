from django.contrib import admin
from django.urls import path
from .views import UserInfoDeleteView, UserInfoDetailView, UserInfoUpdateView

app_name = 'users'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('user_detail/<int:pk>/', UserInfoDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/edit/', UserInfoUpdateView.as_view(), name='user_edit'),
    path('user/<int:pk>/delete/', UserInfoDeleteView.as_view(), name='user_delete'),
]