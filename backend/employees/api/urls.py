from django.urls import include, path
from employees.api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', views.EmployeeViewSet)

app_name = 'employees'
urlpatterns = [
    path('', include(router.urls)),
]
