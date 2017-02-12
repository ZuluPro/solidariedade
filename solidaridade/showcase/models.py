from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class HomeDisplay(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    image = models.ForeignKey('core.Image')
    image_heigth = models.CharField(max_length=10, blank=True)
    image_width = models.CharField(max_length=10, blank=True)
    image_title = models.CharField(max_length=100, blank=True)

    is_active = models.BooleanField(default=False)

    class Meta:
        app_label = "showcase"
        verbose_name = _("home display")
        verbose_name_plural = _("home displays")

    def __str__(self):
        return self.title

    def preview(self):
        return '<img src="%s" height="100px"/>' % self.image.file.url
    preview.short_description = 'Image'
    preview.allow_tags = True

    def html(self):
        return self.text
    html.short_description = _('text')
    html.allow_tags = True
