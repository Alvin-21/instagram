from django import forms
from .models import Image
from cloudinary.models import CloudinaryField

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['posted', 'profile', 'likes']