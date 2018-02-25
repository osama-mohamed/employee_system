from django.conf.urls import url

from .views import (
    AddEmployeeView,
    AllEmployeesView,
    EmployeeDetailView,
    EmployeeUpdateView,
    SalaryUpdateView,
    EmployeeDeleteView,
    AllRelationsView,
    AddRelationView,
    UpdateRelationView,
    DeleteRelationView,
)

urlpatterns = [
    url(r'^add/$', AddEmployeeView.as_view(), name='add'),
    url(r'^$', AllEmployeesView.as_view(), name='all'),
    url(r'^(?P<pk>\d+)/$', EmployeeDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', EmployeeUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/update_salary/$', SalaryUpdateView.as_view(), name='update-salary'),
    url(r'^(?P<pk>\d+)/delete/$', EmployeeDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/relations/$', AllRelationsView.as_view(), name='all-relations'),
    url(r'^(?P<pk>\d+)/add_relation/$', AddRelationView.as_view(), name='add-relation'),
    url(r'^(?P<pk>\d+)/update_relation/$', UpdateRelationView.as_view(), name='update-relation'),
    url(r'^(?P<pk>\d+)/delete_relation/$', DeleteRelationView.as_view(), name='delete-relation'),
]
