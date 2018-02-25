from django.conf.urls import url

from .views import (
    AddEmployeeView,
    AllEmployeesView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    AddRelationView,
)

urlpatterns = [
    url(r'^add/$', AddEmployeeView.as_view(), name='add'),
    url(r'^$', AllEmployeesView.as_view(), name='all'),
    url(r'^(?P<pk>\d+)/$', EmployeeDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', EmployeeUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', EmployeeDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/add_relation/$', AddRelationView.as_view(), name='add-relation'),
]
