from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# Category Model for different categories of pictures
class Category(models.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    @classmethod
    def update_category(cls, cat_id, value):
        cls.objects.filter(id=cat_id).update(name=value)

