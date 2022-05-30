from django import forms
from .models import Image

class UploadForm(forms.ModelForm):
    """
    Form for the image model
    """
    image = forms.ImageField()
    class Meta:
        model = Image
        fields = ('name', 'description', 'image', 'category','location')
