from django.db import models
from django.utils.timezone import now


"""
    Models (Database)
"""
# Create your models here.
class Teachers (models.Model):
    """ Teachers table	"""
    name = models.CharField(max_length=50 , null=True)
    phone = models.CharField(null=True, max_length=14)
    mail = models.EmailField(null = True, max_length=254)
    specialization = models.CharField(max_length=50 , null=True)
    image = models.ImageField(null=True)
    quotes = models.TextField(null = True)
    facebook = models.CharField(max_length=50 , null=True)
    twitter = models.CharField(max_length=50 , null=True)
    google = models.CharField(max_length=50 , null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Teachers"



class Courses (models.Model):
    """ Courses table	"""
    STATUS=(
        ('Available','Available'),
        ('Not Available','Not Available')
    )
    name = models.CharField(max_length=50 , null=True)
    long_description = models.TextField(null=True)
    short_description = models.TextField(null=True)
    price = models.FloatField(null=True)
    min_age = models.IntegerField(null=True)
    max_age = models.IntegerField(null=True)
    cover_image = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    list_image = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    date_created = models.DateTimeField(default=now,editable=False)
    date_update = models.DateTimeField(auto_now=True,editable=False,blank=True)
    status = models.CharField(choices = STATUS, max_length=50,default=STATUS[0])
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Courses"


class Gallery (models.Model):
    """ Images for gallery Table """
    CATEGORY=(
        ('class room','class room'),
        ('competitions','competitions')
    )
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    category = models.CharField(choices=CATEGORY, max_length=50)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Gallery"


class Registeration (models.Model):
    """ Registeration form Table	"""
    STATUS=(
        ('approved','approved'),
        ('pending','pending'),
        ('denied','denied')
    )
    full_name = models.CharField(max_length=50 , null=True)
    birth_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    city = models.CharField(null=True, max_length=50)
    phone_number = models.CharField(null=True, max_length=14)
    secondary_phone_number = models.CharField(null=True,blank=True, max_length=14)
    course = models.ForeignKey(Courses, on_delete = models.SET_NULL, null=True)
    mail = models.EmailField(null=True, max_length=500)
    date_created = models.DateTimeField(default=now,editable=False)
    status = models.CharField(default='pending',choices=STATUS, max_length=50)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Registerations"
class Competition (models.Model):
    STATUS=(
        ('Available','Available'),
        ('Not Available','Not Available')
    )
    name = models.CharField(max_length=50 , null=True)
    long_description = models.TextField(null=True)
    short_description = models.TextField(null=True)
    fees = models.FloatField(null=True)
    student_number = models.IntegerField(null = True)
    min_age = models.IntegerField(null=True)
    max_age = models.IntegerField(null=True)
    cover_image = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    list_image = models.ImageField(null=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    date_created = models.DateTimeField(default=now,editable=False)
    date_update = models.DateTimeField(auto_now=True,editable=False,blank=True)
    date_of_event = models.DateTimeField(null=True)
    status = models.CharField(choices = STATUS, max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Competitions"

class Registeration_Competition (models.Model):
    """ Registeration form Table	"""
    STATUS=(
        ('approved','approved'),
        ('pending','pending'),
        ('denied','denied')
    )
    full_name = models.CharField(max_length=50 , null=True)
    birth_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    city = models.CharField(null=True, max_length=50)
    phone_number = models.CharField(null=True, max_length=14)
    secondary_phone_number = models.CharField(null=True,blank=True, max_length=14)
    competition = models.ForeignKey(Competition, on_delete = models.SET_NULL, null=True)
    mail = models.EmailField(null=True, max_length=500)
    date_created = models.DateTimeField(default=now,editable=False)
    status = models.CharField(default='pending',choices=STATUS, max_length=50)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Registeration Competition"

