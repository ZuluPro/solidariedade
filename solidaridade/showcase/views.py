from django.shortcuts import render
from zinnia.models import Entry


def showcase(request):
    portraits = Entry.objects.filter(categories__title='Portrait',
                                     status=2)
    return render(request, 'showcase.html', {
        'portraits': portraits
    })


def history(request):
    return render(request, 'history.html', {})


def engagement(request):
    return render(request, 'engagement.html', {
        'active': request.GET.get('section', 'children')
    })


def values(request):
    return render(request, 'values.html', {})
