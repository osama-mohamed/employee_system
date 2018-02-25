from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import AddEmployeeForm


class AddEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'employees/add_new_employee.html'
    success_url = reverse_lazy('employees:add')

    def get_context_data(self, **kwargs):
        context = super(AddEmployeeView, self).get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        return context
