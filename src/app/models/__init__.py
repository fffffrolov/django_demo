from django.db import models

from app.models.base import AppModel
from app.models.word_similarity import WordSimilar, WordSimilarityQuerySet

__all__ = [
    'models',
    'AppModel',
    'WordSimilar',
    'WordSimilarityQuerySet',
]
