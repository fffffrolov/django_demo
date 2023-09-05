from django.urls import path, include

from .views import classic, turbo

app_name = 'employees'

turbo_urlpatterns = [
    path('', turbo.EmployeesListView.as_view(), name='list'),
    path('<int:pk>/', turbo.EmployeeDetailView.as_view(), name='detail'),
    path('frames/', turbo.EmployeeListFrameView.as_view(), name='frame-list'),
]

classic_urlpatterns = [
    path('', classic.EmployeesListView.as_view(), name='list'),
    path('<int:pk>/', classic.EmployeeDetailView.as_view(), name='detail'),
]

urlpatterns = [
    path('turbo/', include((turbo_urlpatterns, 'turbo'))),
    path('classic/', include((classic_urlpatterns, 'classic'))),
]
