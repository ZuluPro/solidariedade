from django import forms
from django.core.mail import send_mail
import settings


class ContactForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=3000,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, min_length=0, max_length=30,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(min_length=30, max_length=3000,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))

    def send_mail(self):
        data = self.cleaned_data
        send_mail(subject='[Mail from website] %s',
                  message=data['message'],
                  from_email=data['email'],
                  recipient_list=(settings.CONTACT_EMAIL,))
