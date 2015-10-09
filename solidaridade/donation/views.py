from django.shortcuts import render


def donation(request):
    return render(request, 'donation.html', {})
