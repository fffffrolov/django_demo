from django.urls import include, path

from app.api.schema import schema_view

app_name = 'api_v1'
urlpatterns = [
    path('branches/', include('branches.urls', namespace='v1:branches')),
    path('employees/', include('employees.urls', namespace='v1:employees')),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
