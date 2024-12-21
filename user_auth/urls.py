from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = "user_auth"
urlpatterns = [
    path("", auth_views.LoginView.as_view(
        template_name="authentication/login.html"), name="login"),
    path("register/", views.user_registration, name="register")
]
