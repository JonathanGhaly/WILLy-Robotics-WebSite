from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth.models import User
from courses.models import *
from gallery.models import *
from registeration.models import *
"""
    Forms
"""


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(UserCreationForm):
    """ Registeration of staff form	"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class RegisteredForm(ModelForm):
    """ Status change form	"""
    class Meta:
        model = CourseRegisteration
        fields = ['status']


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'long_description', 'short_description',
                  'price', 'min_age', 'max_age', 'cover_image', 'list_image']


class GalleryForm (forms.ModelForm):

    class Meta:
        model = Gallery
        fields = '__all__'


class CompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'date_of_event': DateInput(),

        }


class CourseEditForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'long_description', 'short_description', 'price',
                  'min_age', 'max_age', 'cover_image', 'list_image', 'status']


class CompetitionEditForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ['name', 'long_description', 'short_description', 'fees',
                  'min_age', 'max_age', 'cover_image', 'list_image', 'status']


class StudentAcceptForm(forms.ModelForm):
    class Meta:
        model = CourseRegisteration
        fields = ['status']


class StudentAcceptFormComp(forms.ModelForm):
    class Meta:
        model = CompetitionRegisteration
        fields = ['status']
