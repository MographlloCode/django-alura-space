from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Picture
from apps.galery.forms import PictureForms

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

    return render(request, 'galery/index.html', {'cards': pictures})

def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User is not authenticated')
        return redirect('login')
    
    form = PictureForms()

    if request.method == 'POST':
        form = PictureForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Picture registered')
            return redirect('home')

    return render(request, 'galery/new-image.html', {"form": form})

def edit_image(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    form = PictureForms(instance=picture)

    if request.method == 'POST':
        form = PictureForms(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            form.save()
            messages.success(request, 'Picture edited successfully')
            return redirect('home')

    return render(request, 'galery/edit-image.html', {'form': form, 'picture_id': picture_id})

def delete_image(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    picture.delete()
    messages.success(request, 'Picture deleted successfully')
    return redirect('home')

def filter(request, category):
    pictures = Picture.objects.filter(published=True, category=category)
    return render(request, 'galery/index.html', {'cards': pictures})