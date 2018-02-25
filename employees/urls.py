from django.conf.urls import url

from .views import (
    AddEmployeeView,
    AllEmployeesView,
    EmployeeDetailView,
)

urlpatterns = [
    url(r'^add/$', AddEmployeeView.as_view(), name='add'),
    url(r'^$', AllEmployeesView.as_view(), name='all'),
    url(r'^(?P<pk>\d+)/$', EmployeeDetailView.as_view(), name='detail'),
]
