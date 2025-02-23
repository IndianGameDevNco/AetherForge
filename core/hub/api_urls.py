from django.urls import path
from .views import ProjectListCreateAPI, ProjectDetailAPI

urlpatterns = [
    path('projects/', ProjectListCreateAPI.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPI.as_view(), name='project-detail'),
]