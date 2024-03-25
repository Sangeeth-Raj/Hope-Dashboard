from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from chief.models import Patient,Therapist,Problem,Solution
from django.utils import timezone
from datetime import date,datetime
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
    return render(request,"index.html")


def login_view(request):
    message =''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            auth_user = User.objects.filter(username=username).first()
            
            if auth_user.check_password(password):
                user = authenticate(request=request,username=username, password=password)
                
                if user is not None:
                    login(request=request,user=user)
                    
                    if Patient.objects.filter(user=user).exists():
                        role = 'patient'
                        return redirect('/user/')
                    elif Therapist.objects.filter(user=user).exists():
                        role = 'therapist'
                        return redirect('/therapist-dashboard/')
                    else:
                        message = "User role doesn't exist"
                else:
                    message = "user doesn't exist"
            else:
                message = "password doesnt match"
        else:
            message = "User not exists"
    context={
        'message' : message,
    }
    return render(request, 'auth/login.html', context)
    
    
def patient_registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if not User.objects.filter(username=phone_number).exists():
                user = User.objects.create_user(username=phone_number,password=password,email=email_id)
                
                patient = Patient.objects.create(
                    name=name,
                    contact_number=phone_number,
                    email=email_id,
                    password=password,
                    joined_from=timezone.now(),
                    user=user,
                )
                login_url = reverse('login')
                return redirect(login_url)
            else:
                return render(request, 'auth/patient_registration.html', {})
        else:
            return render(request, 'auth/patient_registration.html', {})
    else:
        return render(request, 'auth/patient_registration.html', {})
         

def therapist_registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email_id = request.POST.get('email_id')
        qualification = request.POST.get('qualification')
        id_proof = request.POST.get('id_proof')
        location = request.POST.get('location')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        total_year_of_experience = request.POST.get('total_year_of_experience')
        hospital = request.POST.get('hospital')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if not User.objects.filter(username=phone_number).exists():
                user = User.objects.create_user(username=phone_number, password=password, email=email_id)
                user_id = user.pk
                therapist_id = f'THST00{user_id}'
                print(therapist_id, "=========================================")
                therapist = Therapist.objects.create(
                    therapist_id=therapist_id,
                    name=name,
                    contact_number=phone_number,
                    email=email_id,
                    qualification=qualification,
                    id_proof=id_proof,
                    location=location,
                    age=age,
                    gender=gender,
                    total_years_of_experience=total_year_of_experience,
                    hospital_name=hospital,
                    password=password,
                    joined_from=timezone.now(),
                    user=user,
                )
                login_url = reverse('login')
                return redirect(login_url)
            else:
                return render(request, 'auth/therapist-registration.html', {'error_message': 'Phone number already exists'})
        else:
            return render(request, 'auth/therapist-registration.html', {'error_message': "Passwords didn't match"})
    else:
        return render(request, 'auth/therapist-registration.html', {})
    
def register_account(request):
    return render(request,'auth/registerAccount.html',{})


def logout_user(request):
    if request.user.is_authenticated:
        username = request.user.username  # Fetch username before logout
        logout(request)
        message = f'Successfully logged out {username}.'
    else:
        message = 'No user was logged in.'
    return redirect('login') 