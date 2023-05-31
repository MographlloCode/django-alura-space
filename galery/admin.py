from django.contrib import admin
from galery.models import Picture

class ListingPictures(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'subtitle', 'description', 'published',)
    list_display_links = ('id', 'name', 'category', 'subtitle', 'description', )
    search_fields = ('id', 'name', 'category', 'subtitle', 'description', 'published',)
    list_filter = ('category',)
    list_editable = ('published',)
    list_per_page = 10

admin.site.register(Picture, ListingPictures)