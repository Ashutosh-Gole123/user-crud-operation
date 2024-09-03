from django.urls import path
from .views import *

urlpatterns = [
    path('',UserList.as_view()),
    path('<int:pk>/',DetailUser.as_view()),
    path('create/',CreateUser.as_view()),
    path('delete/<int:pk>/',DeleteUser.as_view())
]
