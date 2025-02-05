from django.urls import include, path

urlpatterns = [
    path("users/", include("users.urls")),  # Include the accounts app URLs
]
