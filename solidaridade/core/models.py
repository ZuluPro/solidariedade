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

    def smart_url(self):
        return self.file.url.replace('https://', '//')


class Audio(models.Model):
    file = models.FileField()

    html_template = '<audio controls><source src=%s type="audio/ogg">\
          Your browser does not support the audio tag. </audio>'

    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.file.url

    def listen(self):
        return self.html_template % self.file.url
    listen.short_description = 'Audio'
    listen.allow_tags = True

    def smart_url(self):
        return self.file.url.replace('https://', '//')
