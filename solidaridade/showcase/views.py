from django.shortcuts import render
from zinnia.models import Entry


def showcase(request):
    entries = Entry.published.exclude(image='').order_by('-publication_date')[:2]
    return render(request, 'showcase.html', {
        'latest_entries': entries
    })


def history(request):
    return render(request, 'history.html', {})


def engagement(request):
    return render(request, 'engagement.html', {
        'active': request.GET.get('section', 'children')
    })


def values(request):
    return render(request, 'values.html', {})
