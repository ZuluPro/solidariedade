from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse

from tinymce.widgets import TinyMCE

from showcase import models


class HomeDisplayForm(forms.ModelForm):
    class Meta:
        model = models.HomeDisplay
        fields = '__all__'
        widgets = {
            'text': TinyMCE(attrs={'cols': '100%', 'rows': 5}),
        }


class HomeDisplayAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'is_active')
    form = HomeDisplayForm


admin.site.register(models.HomeDisplay, HomeDisplayAdmin)
