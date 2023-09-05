from django.urls import path

from .views import EmployeeDetailView, EmployeeListFrameView, EmployeeListView

app_name = 'employees'

urlpatterns = [
    path('', EmployeeListView.as_view(), name='list'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='detail'),
    path('frames/', EmployeeListFrameView.as_view(), name='frame-list'),
]
