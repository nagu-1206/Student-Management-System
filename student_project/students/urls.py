from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),

    path('signup/', views.signup, name='signup'),
    path('users/', views.user_list, name='user_list'),

    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('attendance/edit/<int:pk>/', views.edit_attendance, name='edit_attendance'),
    path('attendance/delete/<int:pk>/', views.delete_attendance, name='delete_attendance'),
]
