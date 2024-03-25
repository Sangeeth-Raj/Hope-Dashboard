from django.urls import path
from . import views

urlpatterns = [
    path('', views.therapist_dashboard, name="therapist_dashboard"),
    path('therapist-profile/', views.therapist_profile, name='therapist_profile'),
    path('problems/', views.problems, name="problems"),
    path('problems/<int:problem_id>/', views.view_problem, name="view_problem"),
    path('problems/<int:problem_id>/create-solution', views.post_solution, name="create_solution"),
]
