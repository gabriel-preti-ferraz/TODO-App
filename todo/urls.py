from django.urls import path
from . import views

urlpatterns = [
    path('todo-list/', views.todo_list, name='todo-list'),
    path('todo/<int:todo_id>/', views.todo_view, name='todo'),
]