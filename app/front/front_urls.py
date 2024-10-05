from django.urls import path, re_path
from front import views

urlpatterns = [
    path("", views.index),
    path("signin/", views.sign_in),
    path("app/", views.app),
    re_path(r"^title", views.title),
    re_path(r"^chapter", views.chapter)
]