from django.shortcuts import render
from courses.models import Competition, Course, Teacher
from registeration.models import CourseRegisteration, CompetitionRegisteration
# Create your views here.


def home(request):
    teachers = Teacher.objects.all()
    course = Course.objects.all()
    coursesNum = Course.objects.all().count()
    registerationNum = CourseRegisteration.objects.all().count
    compNum=Competition.objects.all().count()

    context = {
        'courses': course,
        'coursesNum': coursesNum,
        'compNum':compNum,
        'registerationNum': registerationNum,
        'teachers': teachers

    }
    return render(request, 'home/index.html', context)
