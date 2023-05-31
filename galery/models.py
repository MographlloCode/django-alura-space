from django.db import models

class Picture(models.Model):
    ''' Model for Picture '''

    name = models.CharField(max_length=60, null=False, blank=False)
    subtitle = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return f'Picture [name={self.name}]'