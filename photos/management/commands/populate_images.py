import random
from faker import Faker
from django.core.management.base import BaseCommand
from photos.models import Image, Category, Location
from cloudinary.models import CloudinaryField

fake = Faker()

class Command(BaseCommand):
    help = 'Populates the database with 100 provisional images for testing.'

    def handle(self, *args, **kwargs):
        # Create categories
        categories = ['Nature', 'Urban', 'Portrait', 'Abstract', 'Animals', 'Sports', 'Food', 'Travel', 'Art', 'Technology']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)

        # Create locations
        locations = ['New York', 'Paris', 'Tokyo', 'Sydney', 'Cape Town', 'Rio de Janeiro', 'Moscow', 'London', 'Toronto', 'Dubai']
        for location_name in locations:
            Location.objects.get_or_create(name=location_name)

        # Create images
        for _ in range(100):
            image_name = fake.word().capitalize()
            description = fake.sentence(nb_words=10)
            category = random.choice(Category.objects.all())
            location = random.choice(Location.objects.all())

            # Placeholder image URL for testing
            image_url = f'https://res.cloudinary.com/demo/image/upload/v1312461204/sample.jpg'

            # Create and save the image
            Image.objects.create(
                image=image_url,  # Directly assign the URL
                name=image_name,
                description=description,
                category=category,
                location=location,
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 100 provisional images.'))