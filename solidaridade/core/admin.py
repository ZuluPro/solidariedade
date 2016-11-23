from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from zinnia.models import Entry
from zinnia.admin import filters
from zinnia_tinymce.admin import EntryAdminTinyMCE

from core.models import Image, Audio
from core.forms import EntryAdminForm


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'preview', 'smart_url')


class AudioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'listen', 'smart_url')


class EntryAdmin(EntryAdminTinyMCE):
    list_filter = (filters.CategoryListFilter, 'status', 'creation_date',)
    list_display = ('get_title', 'get_categories', 'get_tags',
                    'get_is_visible', 'get_short_url', 'creation_date')

    form = EntryAdminForm
    fieldsets = (
        (_('Content'), {
            'fields': (
                ('title', 'status'),
                'lead',
                'content',
                ('image', 'image_caption'),
                'content_template'
            )}),
        (_('Publication'), {
            'fields': ('creation_date', 'sites'),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Metadatas'), {
            'fields': ('featured', 'excerpt', 'authors', 'related'),
            'classes': ('collapse', 'collapse-closed')}),
        (None, {'fields': (
            'comment_enabled',
            'categories',
            ('tags', 'slug'),
            'pingback_enabled',
            'trackback_enabled',
        )}))

    def get_comment_count(self, obj):
        return obj.comments.count()
    get_comment_count.short_description = _("Comments")


admin.site.register(Image, ImageAdmin)
admin.site.register(Audio, AudioAdmin)

admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdmin)
