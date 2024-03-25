from django.shortcuts import render, get_object_or_404
from .models import Therapist,Patient


def index(request):
    return render(request,"index.html")


def therapist(request):
    single = Therapist.objects.all()
    context = {
        'single' : single
    }
    return render(request,"therapist.html", context)


def single_therapist(request, therapist_id):
    therapist = get_object_or_404(Therapist, therapist_id=therapist_id)
    return render(request, 'therapistSinglePage.html', {'therapist': therapist})


def user(request):
    user_data = Patient.objects.all()
    context = {
        'user_data' : user_data
    }
    return render(request,"user.html", context)

def single_user(request, patient_id):
    user = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, 'singleUserPage.html', {'user': user})