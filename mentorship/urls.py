from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor_list, name='mentor_list'),
    path('send/<int:mentor_id>/', views.send_request, name='send_request'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('cancel/<int:request_id>/', views.cancel_request, name='cancel_request'),
    path('mentor_requests/', views.mentor_requests, name='mentor_requests'),
    path('accept/<int:request_id>/', views.accept_request, name='accept_request'),
    path('reject/<int:request_id>/', views.reject_request, name='reject_request'),
]