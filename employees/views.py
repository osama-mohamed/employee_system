from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import AddEmployeeForm, UpdateEmployeeForm
from .models import Employees


class AddEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'employees/add_new_employee.html'
    success_url = reverse_lazy('employees:all')

    def get_context_data(self, **kwargs):
        context = super(AddEmployeeView, self).get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        return context


class AllEmployeesView(ListView):
    # queryset = Employees.objects.all().order_by('-id')
    template_name = 'employees/all_employees.html'

    def get_queryset(self):
        qs = Employees.objects.filter(activated=True).order_by('-id')
        return qs

    def get_context_data(self, **kwargs):
        context = super(AllEmployeesView, self).get_context_data(**kwargs)
        context['title'] = 'All Employees'
        return context


class EmployeeDetailView(DetailView):
    template_name = 'employees/employee_detail.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'], activated=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee'
        return context


class EmployeeUpdateView(UpdateView):
    form_class = UpdateEmployeeForm
    model = Employees
    template_name = 'employees/employee_update.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'], activated=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Employee'
        return context


class EmployeeDeleteView(DeleteView):
    template_name = 'employees/employee_detail.html'

    def post(self, request, pk):
        qs = Employees.objects.filter(id=pk)
        if qs.exists() and qs.count() == 1:
            user = qs.first()
            user.delete()
            return redirect(reverse('employees:all'))
