from . import views
from django.urls import path

app_name = 'Account'

urlpatterns = [
    path("", views.login, name="login"),
    path("login_confirm", views.login_confirm, name="login_confirm"),
    path("register_confirm", views.register_confirm, name="register_confirm"),
    path("logout_confirm",views.logout_confirm, name="logout_confirm")
]
