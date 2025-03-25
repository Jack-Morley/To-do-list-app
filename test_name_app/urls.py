from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('remove/<int:task_id>/', views.remove_task, name='remove_task'),
]