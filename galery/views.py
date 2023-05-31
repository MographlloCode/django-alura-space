from django.shortcuts import render, get_object_or_404
from galery.models import Picture


def index(request):


    pictures = Picture.objects.order_by('-picture_date').filter(published=True)

    return render(request, 'galery/index.html', {"cards": pictures})

def image(request, picture_id):

    picture = get_object_or_404(Picture, pk=picture_id)

    return render(request, 'galery/image.html', {'picture': picture})

def search(request):
    pictures = Picture.objects.order_by('-picture_date').filter(published=True)

    if 'search' in request.GET:
        search_data = request.GET['search']
        if search_data:
            pictures = pictures.filter(name__icontains=search_data)

    return render(request, 'galery/search.html', {'cards': pictures})