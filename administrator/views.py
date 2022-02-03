from django.shortcuts import render, redirect

from courses.views import competition
from .decorators import unauthenticated_user, allowed_user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import *
from gallery.models import *
from .forms import *
# Create your views here.


@unauthenticated_user
def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('table')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'admin/login.html')

    return render(request, 'admin/login.html')


@login_required(login_url='login')
def AddCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coursetable')
    context = {'forms': form}
    return render(request, 'admin/course-add.html', context)


@login_required(login_url='login')
def AddCompetition(request):
    form = CompetitionForm()
    if request.method == 'POST':
        form = CompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coursetable')
    context = {'forms': form}
    return render(request, 'admin\competition-add.html', context)


@login_required(login_url='login')
def AddImageGal(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('table')
    context = {'forms': form}
    return render(request, 'admin/add-img.html', context)


def LogoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def RegisterationTable(request):
    registerations = CourseRegisteration.objects.order_by(
        'course', 'status', 'date_created', 'full_name', 'birth_date')
    registerationsComp = CompetitionRegisteration.objects.order_by(
        'competition', 'status', 'date_created', 'full_name', 'birth_date')

    context = {
        'registerations': registerations,
        'competitions': registerationsComp
    }
    return render(request, 'admin/admin-registeration-table.html', context)


@login_required(login_url='login')
def CoursesTable(request):
    courses = Course.objects.all()
    competition = Competition.objects.all()
    context = {
        'courses': courses,
        'competition': competition,
    }
    return render(request, 'admin/admin-course-table.html', context)


@login_required(login_url='login')
def DeleteCourse(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('home')
    context = {
        'course': course
    }
    return render(request, 'admin/delete-course.html', context)


@login_required(login_url='login')
def DeleteComp(request, pk):
    competition = Competition.objects.get(id=pk)
    if request.method == 'POST':
        competition.delete()
        return redirect('home')
    context = {
        'competition': competition
    }
    return render(request, 'admin/delete-comp.html', context)


@login_required(login_url='login')
def RegisterSingleView(request, pk):
    student = CourseRegisteration.objects.get(id=pk)
    form = StudentAcceptForm(initial={'status': student})
    if request.method == 'POST':
        form = StudentAcceptForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('table')
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'admin/student-view.html', context)


@login_required(login_url='login')
def RegisterCompSingleView(request, pk):
    student = CompetitionRegisteration.objects.get(id=pk)
    form = StudentAcceptFormComp(initial={'status': student})
    if request.method == 'POST':
        form = StudentAcceptFormComp(
            request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('table')
    context = {
        'student': student,
        'form': form
    }
    return render(request, 'admin/student-comp-view.html', context)
