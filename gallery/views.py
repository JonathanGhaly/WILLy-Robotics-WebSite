from django.shortcuts import render
from .filters import imgFilter
from .models import Gallery
# Create your views here.


def gallery(request):
    img = Gallery.objects.all()
    filter = imgFilter()
    context = {
        'gallery': img,
        'filter': filter
    }

    return render(request, 'gallery/gallery.html', context)
