from django.db import models

# Create your models here.


class Teacher (models.Model):
    """ Teachers table	"""
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(null=True, max_length=14)
    mail = models.EmailField(null=True, max_length=254)
    specialization = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True)
    quotes = models.TextField(null=True)
    facebook = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, null=True)
    google = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Course (models.Model):
    """ Courses table	"""
    STATUS = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )
    name = models.CharField(max_length=50, null=True)
    long_description = models.TextField(null=True)
    short_description = models.TextField(null=True)
    price = models.FloatField(null=True)
    min_age = models.IntegerField(null=True)
    max_age = models.IntegerField(null=True)
    cover_image = models.ImageField(
        null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    list_image = models.ImageField(
        null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=50)

    def __str__(self):
        return self.name


class Competition (models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )
    name = models.CharField(max_length=50, null=True)
    long_description = models.TextField(null=True)
    short_description = models.TextField(null=True)
    fees = models.FloatField(null=True)
    student_number = models.IntegerField(null=True)
    min_age = models.IntegerField(null=True)
    max_age = models.IntegerField(null=True)
    cover_image = models.ImageField(
        null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    list_image = models.ImageField(
        null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_of_event = models.DateTimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=50)

    def __str__(self):
        return self.name
