from branches.api import views
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', views.BranchViewSet)

app_name = 'branches'
urlpatterns = [
    path('', include(router.urls)),
]
