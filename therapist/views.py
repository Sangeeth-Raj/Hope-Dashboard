from django.shortcuts import render,get_object_or_404, redirect
from chief.models import Problem,Solution,Patient,Therapist
from datetime import date,datetime
from django.utils import timezone



# Create your views here.
def therapist_dashboard(request):
    current_user = request.user
    therapist = Therapist.objects.get(user=current_user)
    total_solutions_posted = Solution.objects.count()
    total_solutions = Solution.objects.filter(therapist__user=current_user).count()
    problems_of_patiant = Problem.objects.all()
    context = {
        'total_solutions': total_solutions,
        'total_solutions_posted':  total_solutions_posted,
        'problems': problems_of_patiant
    }
    
    return render(request, "therapistDashboard.html", context)


def problems(request):
    problem_list = Problem.objects.all()
    context = {
        'problem_list' : problem_list
    }
    return render(request,"problems.html", context)


def view_problem(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    solutions = Solution.objects.filter(problem=problem)
    context = {
        'problem': problem,
        'solutions': solutions
    }
    return render(request, 'viewProblem.html', context)


def post_solution(request, problem_id):
    if request.method == 'POST':
        current_user = request.user
        solution = request.POST.get('solution')
        therapist = Therapist.objects.get(user=current_user)
        problem = Problem.objects.get(id=problem_id)
        solution = Solution.objects.create(
            solution=solution,
            therapist=therapist,
            problem=problem,
            date_added=timezone.now(),
        )
        return redirect('view_problem', problem_id=problem_id)
    else:
        return render(request, "viewProblem.html")


def therapist_profile(request):
    try:
        therapist = Therapist.objects.get(user=request.user)
    except Therapist.DoesNotExist:
        therapist = None

    total_solutions = Solution.objects.filter(therapist=therapist).count()

    if request.method == 'GET':
        return render(request, "profile.html", {'therapist': therapist, 'total_solutions': total_solutions})

    elif request.method == 'POST':
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        if therapist:
            therapist.name = name
            therapist.contact_number = contact_number
            therapist.email = email
            therapist.age = age
            therapist.gender = gender
            therapist.save()
        else:
            therapist = Therapist.objects.create(
                user=request.user,
                name=name,
                contact_number=contact_number,
                email=email,
                age=age,
                gender=gender
            )

        return redirect('therapist_profile')