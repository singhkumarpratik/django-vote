from django.urls import path
from .views import UserLoginView, logout_request

app_name = "users"
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_request, name="logout"),
]
