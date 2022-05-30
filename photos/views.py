import django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime
from django.db.models import Q
from .forms import UploadForm
from .models import Image
from django.db.models.base import ObjectDoesNotExist
from django.http  import Http404
# Create your views here.


def home(request):
    photos = Image.objects.all()
    image_basket = {'photos':photos}
    return render(request,'photos/home.html',image_basket)
    
def upload_picture(request):
    
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save()
            image.save()
        
            return redirect('/')
    else:
        form = UploadForm()
    image_basket = {
        'form':form
    }
    return render(request,'photos/upload_picture.html',image_basket)

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "Your search was not found. Enter a valid word."
        return render(request, 'photos/search.html',{"message":message})


