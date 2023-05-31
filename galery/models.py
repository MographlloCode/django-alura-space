from django.db import models
from datetime import datetime

class Picture(models.Model):
    ''' Model for Picture '''

    CATEGORIES = [
        ('NEBULE', 'Nebule',),
        ('STAR', 'Star',),
        ('GALAXY', 'Galaxy',),
        ('PLANET', 'Planet',),
    ]

    name = models.CharField(max_length=60, null=False, blank=False)
    subtitle = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', blank=True)
    category = models.CharField(max_length=60, choices=CATEGORIES, default='')
    published = models.BooleanField(default=False)
    picture_date = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return f'Picture [name={self.name}]'