from django.urls import path
from . import views
#from django.contrib.auth import view as auth_views
urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),

]
