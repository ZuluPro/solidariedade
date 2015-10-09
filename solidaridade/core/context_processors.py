from django.conf import settings as settings_


def settings(request):
    return {'settings': settings_}
