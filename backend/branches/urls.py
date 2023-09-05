from django.urls import path

from .views import BranchDetailView, BranchesListFrameView, BranchesListView

app_name = 'branches'

urlpatterns = [
    path('', BranchesListView.as_view(), name='list'),
    path('<int:pk>/', BranchDetailView.as_view(), name='detail'),
    path('frame/', BranchesListFrameView.as_view(), name='frame-list'),
]
