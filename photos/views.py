from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image, Category

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def home(request):
    categories = Category.objects.all()
    images_by_category = {category.name: Image.objects.filter(category=category) for category in categories}

    return render(request, 'home.html', {'images_by_category': images_by_category})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
    elif 'location' in request.GET and request.GET["location"]:
        location_term = request.GET.get("location")
        searched_images = Image.filter_by_location(location_term)
    else:
        searched_images = Image.objects.all()

    return render(request, 'search.html', {"images": searched_images})
