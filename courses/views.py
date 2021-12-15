from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from administrator.forms import CourseEditForm, CompetitionEditForm
# Create your views here.


def courses(request):
    context = Course.objects.all()
    return render(request, 'courses/courses-list.html', {'courses': context})


def competition(request):
    context = Competition.objects.all()
    return render(request, 'courses/competition-list.html', {'competitions': context})


def singleCourse(request, pk):
    course = Course.objects.get(id=pk)
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
    return render(request, 'courses/courses-single-item.html', context)


def singleComp(request, pk):
    comp = Competition.objects.get(id=pk)
    form = CompetitionEditForm(instance=comp)
    if request.method == 'POST':
        form = CompetitionEditForm(request.POST, request.FILES, instance=comp)
        if form.is_valid():
            comp.date_update = datetime.now()
            form.save()
            return redirect('home')
    context = {
        'competition': comp,
        'form': form
    }
    return render(request, 'courses/competiton-single-item.html', context)
