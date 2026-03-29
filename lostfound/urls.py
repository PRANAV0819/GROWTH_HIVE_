from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='lostfound_list'),
    path('report/', views.report_item, name='report_item'),
]