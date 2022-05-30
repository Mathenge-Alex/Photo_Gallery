from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('uploads',views.upload_picture,name="upload_picture"),
    path('select', views.query_image, name='query_image'),
    re_path(r'^search/', views.search_results,name='search_results'),
    re_path(r'^filter/(\d+)',views.filter_location,name='filter_location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)