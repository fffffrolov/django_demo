"""Read .env file"""
import environ

__all__ = ['env']

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, 'local'),
)

environ.Env.read_env('.env')                  # reading .env file
