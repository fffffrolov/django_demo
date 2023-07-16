from django.urls import path

from .views import BranchDetailView, BranchesListView

app_name = 'branches'

urlpatterns = [
    path('', BranchesListView.as_view(), name='list'),
    path('<int:pk>/', BranchDetailView.as_view(), name='detail'),
]
