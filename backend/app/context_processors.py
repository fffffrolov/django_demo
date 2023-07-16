from django.conf import settings


def enable_turbo(request):
    return {
        "ENABLE_TURBO": settings.ENABLE_TURBO,
    }
