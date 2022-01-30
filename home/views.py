from django.shortcuts import render
from courses.models import Course, Teacher
from registeration.models import CourseRegisteration, CompetitionRegisteration
# Create your views here.


def home(request):
    teachers = Teacher.objects.all()
    coursesNum = Course.objects.all().count()
    if(coursesNum > 0):
         course = Course.objects.get()
    else:
         course = NotImplemented
    registerationNum = CourseRegisteration.objects.all().count

    context = {
        'course': course,
        'coursesNum': coursesNum,
        'registerationNum': registerationNum,
        'teachers': teachers

    }
    return render(request, 'home/index.html', context)
