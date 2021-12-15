from django import forms
from django.shortcuts import render, redirect
from .forms import CompetitionForm, CourseForm
from courses.models import Course, Competition
# Create your views here.


def RegistrationCourse(request):
    form = CourseForm
    if request.method == 'POST':

        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'forms': form}
    return render(request, 'registeration/registeration.html', context)


def RegistrationCoursePk(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(initial={'course': course})
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'registeration/registeration-pk.html', context)


def RegistrationCompetition(request, pk):
    competition = Competition.objects.get(id=pk)
    form = CompetitionForm(initial={'competition': competition})
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'registeration/registration-comp.html', context)
