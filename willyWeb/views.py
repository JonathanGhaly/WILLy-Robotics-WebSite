from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from .decorators import unauthenticated_user, allowed_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime    

# Create your views here.


def home(request):
    course = Courses.objects.all()
    teachers = Teachers.objects.all()
    coursesNum = Courses.objects.all().count()
    registerationNum = Registeration.objects.all().count
    competitionNum = Competition.objects.all().count()
    context = {
        'courses': course,
        'coursesNum': coursesNum,
        'registerationNum': registerationNum,
        'teachers': teachers,
        'competitionNum':competitionNum
    }
    return render(request, 'willyWeb/index.html', context)


def courses(request):
    context = Courses.objects.all()
    return render(request, 'willyWeb/courses-list.html', {'courses': context})


def competition(request):
    context = Competition.objects.all()
    return render(request, 'willyWeb/competition-list.html', {'competitions': context})


def gallery(request):
    img = Gallery.objects.all()
    filter = imgFilter()
    context = {
        'gallery': img,
        'filter': filter
    }

    return render(request, 'willyWeb/gallery.html', context)


def singleCourse(request, pk):
    course = Courses.objects.get(id=pk)
    form = CourseEditForm(instance=course)
    if request.method == 'POST':
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            course.date_update = datetime.now()
            form.save()
            return redirect('home')
    context = {
        'course': course,
        'form': form
    }
    return render(request, 'willyWeb/courses-single-item.html', context)


def singleComp(request, pk):
    comp = Competition.objects.get(id=pk)
    form = CompetitionEditForm(instance=comp)
    if request.method == 'POST':
        form = CompetitionEditForm(request.POST, request.FILES, instance=comp)
        if form.is_valid():
            comp.date_update=datetime.now()
            form.save()
            return redirect('home')
    context = {
        'competition': comp,
        'form':form
    }
    return render(request, 'willyWeb/competiton-single-item.html',context)


def RegistrationCourse(request):
    form = RegisterationForm
    form = RegisterationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'forms': form}
    return render(request, 'willyWeb/registeration.html', context)


def RegistrationCompetition(request, pk):
    competition = Competition.objects.get(id=pk)
    form = RegisterationCompForm(initial={'competition': competition})
    if request.method == 'POST':
        form = RegisterationCompForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'willyWeb/registration-comp.html', context)


def RegistrationCoursePk(request, pk):
    course = Courses.objects.get(id=pk)
    form = RegisterationForm(initial={'course': course})
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'willyWeb/registeration-pk.html', context)


def SignUp(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, 'Account was created for '+user+' successfully')
    context = {'form': form}
    return render(request, 'willyWeb/sign-up.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def AddCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coursetable')
    context = {'forms': form}
    return render(request, 'willyWeb/course-add.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def AddCompetition(request):
    form = CompetitionForm()
    if request.method == 'POST':
        form = CompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coursetable')
    context = {'forms': form}
    return render(request, 'willyWeb\competition-add.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def AddImageGal(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('table')
    context = {'forms': form}
    return render(request, 'willyWeb/add-img.html', context)


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
            return render(request, 'willyWeb/login.html')

    return render(request, 'willyWeb/login.html')


def LogoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def RegisterationTable(request):
    registerations = Registeration.objects.order_by(
        'course', 'status', 'date_created', 'full_name', 'birth_date')
    registerationsComp = Registeration_Competition.objects.order_by(
        'competition', 'status', 'date_created', 'full_name', 'birth_date')

    context = {
        'registerations': registerations,
        'competitions': registerationsComp
    }
    return render(request, 'willyWeb/admin-registeration-table.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def CoursesTable(request):
    courses = Courses.objects.all()
    competition=Competition.objects.all()
    context = {
        'courses': courses,
        'competition':competition,
    }
    return render(request, 'willyWeb/admin-course-table.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def DeleteCourse(request,pk):
    course = Courses.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('home')
    context={
        'course':course
    }
    return render(request,'willyWeb/delete-course.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def DeleteComp(request,pk):
    course = Competition.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('home')
    context={
        'course':course
    }
    return render(request,'willyWeb/delete-comp.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def RegisterSingleView (request,pk):
    student=Registeration.objects.get(id=pk)
    form = StudentAcceptForm(initial={'status':student})
    if request.method == 'POST':
        form = StudentAcceptForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('table') 
    context={
        'student' : student,
        'form':form
    }
    return render(request,'willyWeb/student-view.html',context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def RegisterCompSingleView (request,pk):
    student=Registeration_Competition.objects.get(id=pk)
    form = StudentAcceptFormComp(initial={'status':student})
    if request.method == 'POST':
        form = StudentAcceptFormComp(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('table') 
    context={
        'student' : student,
        'form':form
    }
    return render(request,'willyWeb/student-comp-view.html',context)