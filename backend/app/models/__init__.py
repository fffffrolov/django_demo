from app.models.base import AppModel
from app.models.word_similarity import WordSimilar, WordSimilarityQuerySet
from django.db import models

__all__ = [
    'models',
    'AppModel',
    'WordSimilar',
    'WordSimilarityQuerySet',
]
