from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kanban/',views.kanban, name='kanban'),
    path('tasks/', views.tasks, name='tasks'),
    path('home/',views.home),
    path('room/',views.room)
]    
