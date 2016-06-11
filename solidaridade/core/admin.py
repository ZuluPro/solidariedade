from django.contrib import admin
from core.models import Image, Audio


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'preview')


class AudioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'listen')

admin.site.register(Image, ImageAdmin)
admin.site.register(Audio, AudioAdmin)
