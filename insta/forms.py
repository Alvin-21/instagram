from django import forms
from .models import Image
from cloudinary.models import CloudinaryField

class NewImageForm(forms.ModelForm):
    pic = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}), required=True)

    class Meta:
        model = Image
        fields = ('pic', 'caption')