from django.urls import path
from apps.hotTop import views

urlpatterns = [
    path("hot", views.hot),
    path("test", views.test),
    path("get_all_hot", views.get_all_hot)
]
