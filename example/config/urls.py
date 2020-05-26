from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("comments.urls", namespace="home")),
    path("users/", include("users.urls", namespace="users")),
]
