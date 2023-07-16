"""Read .env file"""
import environ
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent.parent.resolve()
BASE_DIR = str(BASE_PATH)

__all__ = ['env']

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, 'local'),
)

environ.Env.read_env((BASE_PATH.parent / '.env').resolve())
