from django import forms
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
import settings


class ContactForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=3000, label=_("Nom"),
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             required=False)
    phone = forms.CharField(label=_(u"T\xe9l\xe9phone"), required=False, min_length=0, max_length=30,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(min_length=30, max_length=3000, label=_("Message"),
                              widget=forms.Textarea(attrs={'class': 'form-control'}))

    def send_mail(self):
        data = self.cleaned_data
        send_mail(subject='[Mail from website] %s',
                  message=data['message'],
                  from_email=data.get('email', 'noreply@asfp.org'),
                  recipient_list=(settings.CONTACT_EMAIL,))
