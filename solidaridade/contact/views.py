# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html', {
            'form': ContactForm()
        })
    form = ContactForm(data=request.POST)
    if form.is_valid():
        form.send_mail()
        messages.info(request, 'Le message a bien été envoyé')
        return redirect('contact')
    return render(request, 'contact.html', {
        'form': form
    })
