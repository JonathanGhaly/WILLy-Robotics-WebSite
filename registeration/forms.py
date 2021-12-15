from django.forms import ModelForm
from .models import CompetitionRegisteration, CourseRegisteration
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class CompetitionForm(ModelForm):
    class Meta:
        model = CompetitionRegisteration
        fields = ['full_name', 'mail', 'birth_date', 'city',
                  'phone_number', 'secondary_phone_number', 'competition']
        widgets = {
            'birth_date': DateInput(),
        }


class CourseForm(ModelForm):

    """ Registeration for course form	"""
    class Meta:
        model = CourseRegisteration
        fields = ['full_name', 'mail', 'birth_date', 'city',
                  'phone_number', 'secondary_phone_number', 'course']
        widgets = {
            'birth_date': DateInput(),

        }
