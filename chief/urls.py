from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    path('', views.index, name="index"),
    path('therapist/', views.therapist, name="therapist"),
    path('therapist/<str:therapist_id>/', views.single_therapist, name="single_therapist"),
    path('user/', views.user, name="user"),
    path('user/<str:patient_id>/', views.single_user, name="single_user"),
]
