from django.db import models


class Image(models.Model):
    file = models.ImageField()

    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.file.url

    def preview(self):
        return '<img src="%s" height="100px"/>' % self.file.url
    preview.short_description = 'Image'
    preview.allow_tags = True
