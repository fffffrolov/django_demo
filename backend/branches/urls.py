from django.urls import include, path
from rest_framework.routers import SimpleRouter

from branches.api import views

router = SimpleRouter()
router.register('', views.BranchViewSet)

app_name = 'branches'
urlpatterns = [
    path('', include(router.urls)),
]
