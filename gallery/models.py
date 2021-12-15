from django.db import models

# Create your models here.


class Gallery (models.Model):
    """ Images for gallery Table """
    CATEGORY = (
        ('class room', 'class room'),
        ('competitions', 'competitions')
    )
    img = models.ImageField(upload_to=None, height_field=None,
                            width_field=None, max_length=None)
    category = models.CharField(choices=CATEGORY, max_length=50)

    def __str__(self):
        return self.category
