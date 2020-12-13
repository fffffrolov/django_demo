from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

api = [
    path('v1/', include('app.urls.v1', namespace='v1')),
]

urlpatterns = [
    path('api/', include(api)),
    path('admin/', admin.site.urls),
    path('healthchecks/', include('django_healthchecks.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # type: ignore
