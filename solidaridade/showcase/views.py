from django.shortcuts import render
from zinnia.models import Entry


def showcase(request):
    entry = Entry.objects.filter(status=2).exclude(image='').last()
    return render(request, 'showcase.html', {
        'last_entry': entry
    })


def history(request):
    return render(request, 'history.html', {})


def engagement(request):
    return render(request, 'engagement.html', {
        'active': request.GET.get('section', 'children')
    })


def values(request):
    return render(request, 'values.html', {})
