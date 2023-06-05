from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('image/<int:picture_id>', views.image, name='image'),
    path('q', views.search, name='search')
]