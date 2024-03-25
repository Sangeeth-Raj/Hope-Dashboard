from django.shortcuts import render, redirect, get_object_or_404
from datetime import date,datetime
from chief.models import Problem,Solution,Patient,Therapist


def user_dashboard(request):
    current_user = request.user
    problems_count = Problem.objects.filter(patient__user=current_user).count()
    solutions_count = Solution.objects.filter(problem__patient__user=current_user).count()
    solutions = Solution.objects.filter(problem__patient__user=current_user)
    context = {
        'problems_count': problems_count,
        'solutions_count': solutions_count,
        'solutions': solutions
    }
    return render(request, 'userDashboard.html', context)


def profile(request):
    return render(request,"profile.html")


def user_solution(request):
    current_user = request.user
    solutions = Solution.objects.filter(problem__patient__user=current_user)
    context = {
        'solution': solutions
    }
    return render(request, "userSolution.html", context)


def post_problem(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        current_user = request.user
        patient = Patient.objects.get(user=current_user)
        problem = Problem.objects.create(title=title, description=description, patient=patient)
        return redirect('user_solution')
    else:
        return render(request, "userSolution.html")


def user_therapist(request):
    single = Therapist.objects.all()
    context = {
        'single' : single
    }
    return render(request,"userTherapist.html", context)



def user_therapist_single(request, therapist_id):
    therapist = get_object_or_404(Therapist, id=therapist_id)
    return render(request, 'userTherapistSinglePage.html', {'therapist': therapist})


def user_profile(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient = None

    problems_asked = Problem.objects.filter(patient=patient).count()

    if request.method == 'GET':
        return render(request, "patientProfile.html", {'patient': patient, 'problems_asked': problems_asked})

    elif request.method == 'POST':
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        if patient:
            patient.name = name
            patient.contact_number = contact_number
            patient.email = email
            patient.age = age
            patient.gender = gender
            patient.save()
        else:
            patient = Patient.objects.create(
                user=request.user,
                name=name,
                contact_number=contact_number,
                email=email,
                age=age,
                gender=gender
            )

        return redirect('profile')