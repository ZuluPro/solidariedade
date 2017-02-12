from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


@python_2_unicode_compatible
class Title(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    description = models.TextField(max_length=300, verbose_name=_("description"))

    entry_fees = models.PositiveIntegerField(verbose_name=_("entry fees"))
    monthly_contribution = models.PositiveIntegerField(verbose_name=_("monthly contribution"))

    class Meta:
        verbose_name = _('title')
        verbose_name_plural = _('titles')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # birth_date = models.DateField(null=True, verbose_name=_("birth date"))

    country = CountryField(verbose_name=_("country"))
    address = models.TextField(max_length=300, verbose_name=_("address"))
    postal_code = models.CharField(max_length=20, verbose_name=_("postal code"))
    city = models.CharField(max_length=70, verbose_name=_("city"))

    phone_number = PhoneNumberField(verbose_name=_("phone number"))

    title = models.ForeignKey(Title)

    subscription_date = models.DateField(default=now, blank=True, null=True, verbose_name=_("subscription date"))

    validated = models.BooleanField(default=False, verbose_name=_('validated'))
    validation_date = models.DateField(blank=True, null=True, verbose_name=_("validation date"))

    unsubscripted = models.BooleanField(default=False, verbose_name=_('unsubscripted'))
    unsubscription_date = models.DateField(blank=True, null=True, verbose_name=_("unsubscription date"))

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email


METHODS = (
    ('paypal', _("Paypal")),
    ('check', _("check")),
    ('cash', _("cash")),
    ('natural', _("natural")),
    ('bank-transfer', _("bank transfer")),
    ('electronic', _("electronic payment")),
)


@python_2_unicode_compatible
class Contribution(models.Model):
    member = models.ForeignKey(Member, verbose_name=_("member"))
    note = models.TextField(max_length=500, null=True, blank=True, verbose_name=_("note"))
    sum = models.PositiveIntegerField(verbose_name=_("sum"))

    pledge_date = models.DateField(auto_now_add=True, verbose_name=_("pledge date"))
    due_date = models.DateField(blank=True, null=True, verbose_name=_("due date"))
    paid = models.BooleanField(default=False, verbose_name=_('paid'))
    payment_date = models.DateField(blank=True, null=True, verbose_name=_("payment date"))
    payment_method = models.CharField(max_length=20, blank=True, null=True, choices=METHODS, verbose_name=_('payment method'))

    class Meta:
        verbose_name = _('contribution')
        verbose_name_plural = _('contributions')

    def __str__(self):
        return "%s %s" % (self.member, self.sum)

    def get_public_id(self):
        return "{}{:0>5}".format(self.pledge_date.strftime('%Y%m%d'), self.member.id)
