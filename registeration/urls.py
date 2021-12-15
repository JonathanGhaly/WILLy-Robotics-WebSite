from django.urls import path
from . import views
#from django.contrib.auth import view as auth_views
urlpatterns = [
    path('RegisterationCompetition/<str:pk>',
         views.RegistrationCompetition, name='Apply-comp'),
    path('Registeration/', views.RegistrationCourse, name='Apply'),
    path('Registeration/<str:pk>', views.RegistrationCoursePk, name='Apply-pk'),
]
