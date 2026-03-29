from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.create_project, name='create_project'),
    path('join/<int:project_id>/', views.send_join_request, name='send_join_request'),
    path('project_requests/', views.project_requests, name='project_requests'),
    path('accept/<int:request_id>/', views.accept_join, name='accept_join'),
    path('reject/<int:request_id>/', views.reject_join, name='reject_join'),
    path('my_projects/', views.my_projects, name='my_projects'),
    
]