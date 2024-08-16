from django.contrib import admin
from django.utils.html import format_html
from .models import Image, Category, Location

class ImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'category', 'location', 'upload_date')
    list_filter = ('category', 'location', 'upload_date')
    search_fields = ('name', 'description')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return '-'
    thumbnail.short_description = 'Thumbnail'

admin.site.register(Image, ImageAdmin)

admin.site.register(Category)
admin.site.register(Location)