from django.urls import path
from . import views

urlpatterns = [
    path('users/actions/', views.ActionList.as_view()),
]