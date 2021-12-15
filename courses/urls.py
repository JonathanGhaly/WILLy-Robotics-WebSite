from django.urls import path
from . import views
urlpatterns = [
    path('courses/', views.courses, name='course-list'),
    path('course/<str:pk>/', views.singleCourse, name="course"),
    path('competitons/', views.competition, name='competition-list'),
    path('competiton/<str:pk>/', views.singleComp, name="competition"), ]
