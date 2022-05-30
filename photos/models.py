from django.db import models
from cloudinary.models import CloudinaryField
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# Category Model for different categories of pictures
class Category(models.Model):
    
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    @classmethod
    def update_category(cls, cat_id, value):
        cls.objects.filter(id=cat_id).update(name=value)

# Location Model
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    location = models.ForeignKey(Location ,on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        update = cls.objects.filter(id=id).update(image=image)
        return update
    
    @classmethod
    def update_image_name(cls,id,name):
        update =cls.objects.filter(id=id).update(name=name)
        return update

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

# Ordering by upload date
    class Meta:
        ordering = ['-upload_date']

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location