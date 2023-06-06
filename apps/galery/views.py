from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Picture

from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User is not authenticated')
        return redirect('login')

    pictures = Picture.objects.order_by('-picture_date').filter(published=True)

    return render(request, 'galery/index.html', {"cards": pictures})

def image(request, picture_id):

    picture = get_object_or_404(Picture, pk=picture_id)

    return render(request, 'galery/image.html', {'picture': picture})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User is not authenticated')
        return redirect('login')
    
    pictures = Picture.objects.order_by('-picture_date').filter(published=True)

    if 'search' in request.GET:
        search_data = request.GET['search']
        if search_data:
            pictures = pictures.filter(name__icontains=search_data)

    return render(request, 'galery/search.html', {'cards': pictures})