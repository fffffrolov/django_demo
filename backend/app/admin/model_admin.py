# type: ignore
from typing import Optional, Tuple

from django import forms
from django.contrib import admin
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.db.models import Model
from django.http import HttpRequest
from django.urls import NoReverseMatch, reverse
from django.utils.safestring import SafeText, mark_safe
from django.utils.translation import gettext_lazy as _
from django_admin_inline_paginator.admin import TabularInlinePaginated
from mapwidgets.widgets import GooglePointFieldWidget


class CustomSearchMixin:
    """
    Customize admin search by specified in model QuerySet method
    """

    def get_search_results(self,
                           request: HttpRequest,
                           queryset: models.QuerySet,
                           search_term: str) -> Tuple[models.QuerySet, bool]:
        if hasattr(queryset, 'search') and callable(queryset.search):
            if search_term:
                return queryset.search(search_term), False
        return super().get_search_results(request, queryset, search_term)


class AdminLinksMixin:
    @staticmethod
    def admin_edit_url(instance: Model) -> Optional[str]:
        """
        Return instance admin changing page if exists
        """
        _meta = instance._meta
        try:
            return reverse(f'admin:{_meta.app_label}_{_meta.model_name}_change', args=(instance.pk,))
        except NoReverseMatch:
            return None

    def admin_edit_link(self, instance: Model, text: str = 'Edit', target: str = '_top') -> Optional[SafeText]:
        """
        Return html link to instance admin page if exists
        """
        url = self.admin_edit_url(instance)
        return mark_safe(f"<a target='{target}' href='{url}'>{text}</a>") if url is not None else None


class AdminFormsMixin:
    """
    Override default admin forms
    """
    formfield_overrides = {
        models.BooleanField: {
            'widget': forms.Select(choices=[(True, _('Yes')), (False, _('No'))]),
        },
        models.NullBooleanField: {
            'widget': forms.Select(choices=[(True, _('Yes')), (False, _('No')), (None, _('-----'))]),
        },
        gis_models.PointField: {
            'widget': GooglePointFieldWidget,
        },
        gis_models.GeometryField: {
            'widget': GooglePointFieldWidget,
        },
    }


class AppModelAdmin(CustomSearchMixin,
                    AdminLinksMixin,
                    AdminFormsMixin,
                    admin.ModelAdmin):
    pass


class AppTabularInlinePaginated(AdminLinksMixin,
                                AdminFormsMixin,
                                TabularInlinePaginated):
    pass


class AppTabularInline(AdminLinksMixin,
                       AdminFormsMixin,
                       admin.TabularInline):
    pass


class AppStackedInline(AdminLinksMixin,
                       AdminFormsMixin,
                       admin.StackedInline):
    pass
