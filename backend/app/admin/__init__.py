# type: ignore
from app.admin.model_admin import AppModelAdmin, AppStackedInline, AppTabularInline, AppTabularInlinePaginated
from django.contrib import admin

__all__ = [
    'admin',
    'AppModelAdmin',
    'AppStackedInline',
    'AppTabularInline',
    'AppTabularInlinePaginated',
]
