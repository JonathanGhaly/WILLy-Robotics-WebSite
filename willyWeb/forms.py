from django.forms import ModelForm
from .models import Registeration,Courses,Gallery
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
        fields = '__all__'

class GalleryForm (forms.ModelForm):
    
    class Meta:
        model = Gallery
        fields = '__all__'
