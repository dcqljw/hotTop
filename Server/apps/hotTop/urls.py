from django.urls import path
from apps.hotTop import views

urlpatterns = [
    path("hot", views.hot),
    path("test", views.test)
]
