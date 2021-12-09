from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/actions/', views.ActionList.as_view()),
    path('users/projects/', views.ProjectList.as_view()),
    # re_path(r'^users/actions/focused/$', views.FocusedActionList.as_view()),
]