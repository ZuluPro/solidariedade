from django.contrib import admin
from core.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'preview')

admin.site.register(Image, ImageAdmin)
