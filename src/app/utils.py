import uuid
from os import path

from django.utils.deconstruct import deconstructible


@deconstructible
class RandomPath:
    def __init__(self, prefix: str = ''):
        self.prefix = prefix

    def __call__(self, _, filename):
        name = uuid.uuid4()
        extension = path.splitext(filename)[1]

        return path.join(self.prefix, f'{name}{extension}')
