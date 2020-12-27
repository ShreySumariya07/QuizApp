from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Account/",include("Account.urls")),
    path("Quiz/",include("Quiz.urls")),
]