from django.urls import include, path
from rest_framework.routers import SimpleRouter

from employees.api import views

router = SimpleRouter()
router.register('', views.EmployeeViewSet)

app_name = 'employees'
urlpatterns = [
    path('', include(router.urls)),
]
