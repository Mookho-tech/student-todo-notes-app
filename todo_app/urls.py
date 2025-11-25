from django.urls import path
from . import views

urlpatterns = [
    # Dashboard & Auth
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),  # uncommented, create view

    # Tasks
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:task_id>/add-to-calendar/', views.create_calendar_event, name='task_add_to_calendar'),

    # Notes
    path('notes/', views.note_list, name='note_list'),
    path('notes/create/', views.note_create, name='note_create'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('notes/<int:pk>/edit/', views.note_update, name='note_update'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),

    # Calendar
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/create/', views.create_calendar_event, name='create_calendar_event'),
]
