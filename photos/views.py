import django
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.


class HomeView(TemplateView):
    template_name = 'photos/home.html'