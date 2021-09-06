from django.forms import ModelForm
from .models import Registeration,Courses,Gallery,Competition,Registeration_Competition
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth.models import User

"""
    Forms
"""

class DateInput(forms.DateInput):
    input_type = 'date'
    
class RegisterationForm(ModelForm):
    
    """ Registeration for course form	"""
    class Meta:
        model = Registeration
        fields = ['full_name','mail','birth_date','city','phone_number','secondary_phone_number','course']
        widgets = {
            'birth_date': DateInput(),
            
        }

class RegisterationCompForm(ModelForm):
    class Meta:
        model = Registeration_Competition
        fields = ['full_name','mail','birth_date','city','phone_number','secondary_phone_number','competition']
        widgets = {
        'birth_date': DateInput(),        
        }
class UserForm(UserCreationForm):
    """ Registeration of staff form	"""
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
class RegisteredForm(ModelForm):
    """ Status change form	"""
    class Meta:
        model = Registeration
        fields = ['status']

class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Courses
        fields = ['name','long_description','short_description','price','min_age','max_age','cover_image','list_image']

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
        model = Courses
        fields = ['name','long_description','short_description','price','min_age','max_age','cover_image','list_image','status']
class CompetitionEditForm(forms.ModelForm):
    
    class Meta:
        model = Competition
        fields = ['name','long_description','short_description','fees','min_age','max_age','cover_image','list_image','status']

class StudentAcceptForm(forms.ModelForm):
    class Meta:
        model = Registeration
        fields = ['status']
class StudentAcceptFormComp(forms.ModelForm):
    class Meta:
        model = Registeration_Competition
        fields = ['status']