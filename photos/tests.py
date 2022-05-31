from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,Category,Location



class CategoryTestClass(TestCase):
    #setup Test
    def setUp(self):
        self.category = Category(name='Technology')
        
        # Deleting an object
    def tearDown(self):
        Category.objects.all().delete()
        
        # Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
        
        # Saving
    def test_save_method(self):
        self.category.save_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
        #Deleting Category
    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
    
        # Updating a Category
    def test_update_category(self):
        self.category.save_category()
        new_name="Tech"
        self.category.update_category(self.category.id,new_name)
        update = Category.objects.get(name="Tech")
        self.assertEquals(update.name,"Tech")