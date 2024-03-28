"""
URL configuration for Hope_Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import login_view, patient_registration, therapist_registration, register_account, logout_user

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('register-account/', register_account, name='register-account'),
    path('login/', login_view, name='login'),
    path('user-admin/', include('chief.urls')),
    path('therapist-dashboard/', include('therapist.urls')),
    path('user/', include('client.urls')),
    path('therapist-registration/', therapist_registration, name='therapist-registration'),
    path('patient-registration/', patient_registration, name='patient-registration'),
    path('logout/', logout_user, name='logout_user'),
]
