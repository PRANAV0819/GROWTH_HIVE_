from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('upload/', views.upload_resource, name='upload_resource'),
]