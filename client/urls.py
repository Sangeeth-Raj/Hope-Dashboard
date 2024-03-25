from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name="user_dashboard"),
    path('profile', views.user_profile, name="profile"),
    path('solutions/', views.user_solution, name="user_solution"),
    path('create-problem/', views.post_problem, name="create_problem"),
    path('therapist/', views.user_therapist, name="user_therapist"),
    path('therapist/profile/', views.user_therapist_single, name='user_therapist_single'),
    path('therapist/profile/<int:therapist_id>/', views.user_therapist_single, name='user_therapist_single'),
]
