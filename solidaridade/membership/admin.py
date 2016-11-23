from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from membership import models


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'entry_fees', 'monthly_contribution')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'country', 'validated',
                    'unsubscripted')
    list_filter = ('title',
                   'validated', 'validation_date',
                   'unsubscripted', 'unsubscription_date')
    fieldsets = (
        (None, {
            'fields': (
                ('first_name', 'last_name', 'birth_date', 'title',),
                ('country', 'postal_code', 'city'),
                'address',
                ('phone_number', 'email')
            ),
        }),
        (_('Subscription'), {
            'fields': (
                'subscription_date',
                ('validation_date', 'validated'),
                ('unsubscription_date', 'unsubscripted')
            ),
        }),
    )


class ContributionAdmin(admin.ModelAdmin):
    date_hierachy = 'due_date'
    list_display = ('member', 'sum', 'due_date', 'paid', 'payment_date',
                    'payment_method')
    list_filter = ('due_date', 'payment_date', 'paid', 'payment_method')
    fieldsets = (
        (None, {
            'fields': (
                ('member', 'sum', 'due_date'),
                'note',
                ('payment_date', 'paid', 'payment_method')
            ),
        }),
    )


admin.site.register(models.Title, TitleAdmin)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Contribution, ContributionAdmin)
