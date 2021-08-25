from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from .decorators import unauthenticated_user,allowed_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    course = Courses.objects.get(id=1)
    teachers = Teachers.objects.all()
    coursesNum = Courses.objects.all().count()
    registerationNum = Registeration.objects.all().count
    context = {
        'course': course,
        'coursesNum':coursesNum,
        'registerationNum':registerationNum,
        'teachers':teachers

    }
    return render(request, 'willyWeb/index.html',context)


def courses(request):
    context = Courses.objects.all()
    return render(request, 'willyWeb/courses-list.html', {'courses': context})


def gallery(request):
    img = Gallery.objects.all()
    filter = imgFilter()
    context = {
        'gallery':img,
        'filter':filter
    }
    
    return render(request, 'willyWeb/gallery.html', context)


def singleCourse(request, pk):
    course = Courses.objects.get(id=pk)
    return render(request, 'willyWeb/courses-single-item.html', {'course': course})


def RegistrationCourse(request):
    form = RegisterationForm
    form = RegisterationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'forms': form}
    return render(request, 'willyWeb/registeration.html', context)


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
            messages.success(request,'Account was created for '+user+' successfully')
    context = {'form':form}
    return render(request, 'willyWeb/sign-up.html',context)


def AddCourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coursetable')
    context = {'forms': form}
    return render(request, 'willyWeb/course-add.html', context)

def AddImageGal(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST)
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
        user = authenticate(request,username = username, password = password)
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
    registerations = Registeration.objects.order_by('course', 'status','full_name','birth_date')
    
    context={
        'registerations':registerations
    }
    return render(request, 'willyWeb/admin-registeration-table.html',context)
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def CoursesTable(request):
    courses = Courses.objects.all()
   
    context={
        'courses':courses,
    }
    return render(request, 'willyWeb/admin-course-table.html',context)
