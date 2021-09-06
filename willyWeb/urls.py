from django.urls import path
from . import views
#from django.contrib.auth import view as auth_views
urlpatterns = [
    path('', views.home, name='home'),
#ADMIN Pages
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('logout/', views.LogoutUser, name='logout'),
    #path('reset_password',auth_views.PasswordResetView.as_view() , name='reset_password'),
    #path('reset_password_sent',auth_views.PasswordResetDoneView.as_view() , name = 'password_reset_done'),
    #path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    #path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view() , name= 'password_reset_complete'),


    path('registration-admin',views.RegisterationTable,name='table'),
    path('coursetable',views.CoursesTable,name='coursetable'),
    path('add_course/', views.AddCourse, name='add-course'),
    path('add_image/', views.AddImageGal, name='add-image'),
    path('add_competition/', views.AddCompetition, name='add-competition'),
    path('delete-course/<str:pk>/', views.DeleteCourse, name="delete-course"),
    path('student-course/<str:pk>/', views.RegisterSingleView, name="student-course"),
    path('student-competition/<str:pk>/', views.RegisterCompSingleView, name="student-competition"),

    path('delete-competition/<str:pk>/', views.DeleteComp, name="delete-comp"),

#######################################################################
#Course pages
    path('courses/', views.courses, name='course-list'),
    path('course/<str:pk>/', views.singleCourse, name="course"),
    path('competitons/', views.competition, name='competition-list'),
    path('competition/<str:pk>/', views.singleComp, name="competition"),
    path('RegisterationCompetition/<str:pk>', views.RegistrationCompetition, name='Apply-comp'),
########################################################################
#Registration course
    path('Registeration/', views.RegistrationCourse, name='Apply'),
    path('Registeration/<str:pk>', views.RegistrationCoursePk, name='Apply-pk'),
#########################################################################################
    path('gallery/', views.gallery, name='gallery'),

]
