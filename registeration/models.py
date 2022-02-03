from django.db import models
from courses.models import Competition, Course
from django.utils.timezone import now

# Create your models here.


class CourseRegisteration (models.Model):
    """ Registeration form Table	"""
    STATUS = (
        ('approved', 'approved'),
        ('pending', 'pending'),
        ('denied', 'denied')
    )
    full_name = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(
        null=True, auto_now=False, auto_now_add=False)
    city = models.CharField(null=True, max_length=50)
    phone_number = models.CharField(null=True, max_length=14)
    secondary_phone_number = models.CharField(
        null=True, blank=True, max_length=14)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    mail = models.EmailField(null=True, max_length=500)
    date_created = models.DateTimeField(default=now, editable=False)
    status = models.CharField(default='pending', choices=STATUS, max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Registerations"


class CompetitionRegisteration (models.Model):
    """ Registeration form Table	"""
    STATUS = (
        ('approved', 'approved'),
        ('pending', 'pending'),
        ('denied', 'denied')
    )
    full_name = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(
        null=True, auto_now=False, auto_now_add=False)
    city = models.CharField(null=True, max_length=50)
    phone_number = models.CharField(null=True, max_length=14)
    secondary_phone_number = models.CharField(
        null=True, blank=True, max_length=14)
    competition = models.ForeignKey(
        Competition, on_delete=models.SET_NULL, null=True)
    mail = models.EmailField(null=True, max_length=500)
    date_created = models.DateTimeField(default=now, editable=False)
    status = models.CharField(default='pending', choices=STATUS, max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Registeration Competition"
