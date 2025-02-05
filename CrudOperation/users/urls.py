from django.urls import path
from .views import reset_password_view

urlpatterns = [
    path("reset-password/", reset_password_view, name="reset-password"),
]
