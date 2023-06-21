from django import forms
from apps.galery.models import Picture

class PictureForms(forms.ModelForm):
  class Meta:
    model = Picture
    exclude = ['published',]
    labels = {
      'name': 'Name',
      'subtitle': 'Subtitle',
      'description': 'Description',
      'category': 'Category',
      'picture': 'Select your picture',
      'picture_date': 'When you took the shot?',
      'user': 'User'
    }
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
      'picture': forms.FileInput(attrs={'class': 'form-control'}),
      'picture_date': forms.DateInput(
          format='%d/%m/%Y',
          attrs={
            'type': 'date',
            'class': 'form-control'
          }
        ),
      'user': forms.Select(attrs={'class': 'form-control'}),
    }