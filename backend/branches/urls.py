from django.shortcuts import redirect
from django.urls import path, include, reverse

from .views import classic, turbo

app_name = 'branches'


def redirect_to_classic(_):
    return redirect(reverse('branches:classic:list'), permanent=True)


turbo_urlpatterns = [
    path('', turbo.BranchesListView.as_view(), name='list'),
    path('<int:pk>/', turbo.BranchDetailView.as_view(), name='detail'),
    path('frame/', turbo.BranchesListFrameView.as_view(), name='frame-list'),
]

classic_urlpatterns = [
    path('', classic.BranchesListView.as_view(), name='list'),
    path('<int:pk>/', classic.BranchDetailView.as_view(), name='detail'),
]

urlpatterns = [
    path('', redirect_to_classic, name='home'),
    path('turbo/', include((turbo_urlpatterns, 'turbo'))),
    path('classic/', include((classic_urlpatterns, 'classic'))),
]
