from django import forms
from .models import Image, Category, Location

class ImageUploadForm(forms.ModelForm):
    new_category = forms.CharField(max_length=30, required=False, label="Or add a new category")
    new_location = forms.CharField(max_length=30, required=False, label="Or add a new location")

    class Meta:
        model = Image
        fields = ['image', 'name', 'description', 'category', 'location']

    def save(self, commit=True):
        category = self.cleaned_data.get('new_category')
        location = self.cleaned_data.get('new_location')

        if category:
            category_obj, created = Category.objects.get_or_create(name=category)
            self.instance.category = category_obj

        if location:
            location_obj, created = Location.objects.get_or_create(name=location)
            self.instance.location = location_obj

        return super().save(commit=commit)
