import django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime
from django.db.models import Q
from .forms import UploadForm

from .models import Image

# Create your views here.


class HomeView(TemplateView):
    template_name = 'photos/home.html'
    photos = Image.objects.all()
    inf = {'photos':photos}
    
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
    inf = {
        'form':form
    }
    return render(request,'pictures/upload_picture.html',inf)
