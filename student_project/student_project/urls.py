from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # 🔐 Login
    path('login/', auth_views.LoginView.as_view(
        template_name='students/login.html'
    ), name='login'),

    # 🔐 Logout (FORCE redirect to login page)
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    # Students App
    path('', include('students.urls')),
]
