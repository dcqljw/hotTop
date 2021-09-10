from django.urls import path

from apps.UserAuth import views

urlpatterns = [
    path("login", views.login)
]
