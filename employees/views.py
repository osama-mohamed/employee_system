from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
)
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import AddEmployeeForm
from .models import Employees


class AddEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'employees/add_new_employee.html'
    success_url = reverse_lazy('employees:add')

    def get_context_data(self, **kwargs):
        context = super(AddEmployeeView, self).get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        return context


class AllEmployeesView(ListView):
    queryset = Employees.objects.all().order_by('-id')
    template_name = 'employees/all_employees.html'

    def get_context_data(self, **kwargs):
        context = super(AllEmployeesView, self).get_context_data(**kwargs)
        context['title'] = 'All Employees'
        return context


class EmployeeDetailView(DetailView):
    template_name = 'employees/all_employees.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee'
        return context
