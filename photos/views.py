from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm
from .models import Image, Category
from django.core.paginator import Paginator
from django.http import JsonResponse


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"message": "Image uploaded successfully!"})
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def home(request):
    categories = Category.objects.all()
    images_by_category = {category.name: Image.objects.filter(category=category) for category in categories}

    # Paginate the images in each category
    for category, images in images_by_category.items():
        paginator = Paginator(images, 10)  # Show 10 images per page
        page_number = request.GET.get(f'page_{category}')
        images_by_category[category] = paginator.get_page(page_number)

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


# Delete Images
@login_required
def delete_image(request, image_id):
    if request.user.is_staff:
        image = get_object_or_404(Image, id=image_id)
        image.delete()
    return redirect('home')