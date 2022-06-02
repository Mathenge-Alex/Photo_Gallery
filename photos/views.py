import django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime
from django.db.models import Q
from .forms import UploadForm
from .models import Image
from django.db.models.base import ObjectDoesNotExist
from django.http  import Http404
import pyperclip as clip

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


def query_image(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    images = Image.objects.filter(
        Q(category__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        ) 
    message = f"{q}"
    return render(request, 'photos/search.html',{"message":message,"photos": images})

def filter_location(request,location_id):
    try:
        locations = {'1':"Kenya",'2':"USA",'3':"Canada",'4':"China",'5':"Bahamas"}   
    
        filtered_photos = Image.objects.filter(location__name__icontains=locations.get(str(location_id))) 
        message = f"{locations.get(location_id)}"
    except  ObjectDoesNotExist:
        raise Http404()
    return render(request,'photos/filter_location.html',{"message":message,"photos": filtered_photos})