# from django.shortcuts import render
# from rest_framework import generics
# from .serializers import *
# from .models import *

# # Crud Operations
# #Get 
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# #PUT
# class DetailUser(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# #POST
# class CreateUser(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# #DELETE
# class DeleteUser(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import reset_user_password

@csrf_exempt
def reset_password_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            if not email:
                return JsonResponse({"error": "Email is required"}, status=400)
            
            # Call the reset function
            result = reset_user_password(email)
            return JsonResponse({"message": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)
