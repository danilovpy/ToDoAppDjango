from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('delete/<int:task_id>', views.delete_task, name='delete'),
]