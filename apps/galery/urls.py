from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('image/<int:picture_id>', views.image, name='image'),
    path('q', views.search, name='search'),
    path('new-image', views.new_image, name='new_image'),
    path('edit-image/<int:picture_id>', views.edit_image, name='edit_image'),
    path('delete-image/<int:picture_id>', views.delete_image, name='delete_image'),
    path('filter/<str:category>', views.filter, name='filter'),
]