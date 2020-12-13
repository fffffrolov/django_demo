from django.contrib import admin

from app.admin.model_admin import AppModelAdmin, AppStackedInline, AppTabularInline

__all__ = [
    'admin',
    'AppModelAdmin',
    'AppStackedInline',
    'AppTabularInline',
]
