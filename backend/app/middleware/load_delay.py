import logging
import time

from django.conf import settings

logger = logging.getLogger(__name__)


class LoadDelayMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if settings.DEFAULT_LOAD_DELAY:
            time.sleep(settings.DEFAULT_LOAD_DELAY)
            logger.debug(f'Artificial delay: {settings.DEFAULT_LOAD_DELAY}')

        return response
