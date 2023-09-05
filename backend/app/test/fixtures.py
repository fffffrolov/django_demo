import shutil
import tempfile
from pathlib import Path

import pytest
from app.test.factories import UserFactory
from django.conf import settings
from rest_framework.test import APIClient


@pytest.fixture(scope='session', autouse=True)
def _clean_media():
    settings.MEDIA_ROOT = Path(tempfile.gettempdir(), 'demo/media')
    Path(settings.MEDIA_ROOT).mkdir(parents=True, exist_ok=True)
    yield
    shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)


@pytest.fixture
def user(db):
    return UserFactory()


@pytest.fixture
def api_client(db, user):
    api_client = APIClient()
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)
