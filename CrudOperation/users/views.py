from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Crud Operations
#Get 
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#PUT
class DetailUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#POST
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#DELETE
class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
