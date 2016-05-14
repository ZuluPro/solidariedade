from django.shortcuts import render
from zinnia.models import Entry


def actions(request):
    actions = Entry.published.filter(categories__slug='action')
    return render(request, 'actions.html', {
        'object_list': actions,
    })
