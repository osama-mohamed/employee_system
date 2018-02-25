from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
)
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import AddEmployeeForm, UpdateEmployeeForm, AddRelationForm, UpdateSalaryForm
from .models import Employees, Relationship


class AddEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'employees/add_new_employee.html'
    success_url = reverse_lazy('employees:all')

    def get_context_data(self, **kwargs):
        context = super(AddEmployeeView, self).get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        return context


class AllEmployeesView(ListView):
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


class SalaryUpdateView(UpdateView):
    form_class = UpdateSalaryForm
    model = Employees
    template_name = 'employees/employee_update.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'], activated=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super(SalaryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Salary'
        return context



class EmployeeDeleteView(DeleteView):
    template_name = 'employees/employee_detail.html'

    def post(self, request, pk):
        qs = Employees.objects.filter(id=pk)
        if qs.exists() and qs.count() == 1:
            user = qs.first()
            user.delete()
            return redirect(reverse('employees:all'))


class AddRelationView(View):
    form_class = AddRelationForm
    template_name = 'employees/add_new_relation.html'

    def get(self, request, pk):
        form = self.form_class(None)
        context = {
            'form': form,
            'title': 'Add Relation'
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            qs = Employees.objects.filter(id=pk, activated=True).first()
            relation = Relationship.objects.create(
                employee=qs,
                relationship_type=form.cleaned_data.get('relationship_type'),
                name=form.cleaned_data.get('name'),
                age=form.cleaned_data.get('age'),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
            )
            return redirect('employees:all')


class AllRelationsView(ListView):
    template_name = 'employees/all_relations.html'

    def get_queryset(self):
        qs = Relationship.objects.filter(employee_id=self.kwargs['pk']).order_by('-id')
        return qs

    def get_context_data(self, **kwargs):
        context = super(AllRelationsView, self).get_context_data(**kwargs)
        context['title'] = 'All Relations'
        return context


class UpdateRelationView(UpdateView):
    form_class = AddRelationForm
    model = Relationship
    template_name = 'employees/add_new_relation.html'
    success_url = reverse_lazy('employees:all')

    def get_queryset(self):
        qs = Relationship.objects.filter(id=self.kwargs['pk'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(UpdateRelationView, self).get_context_data(**kwargs)
        context['title'] = 'Update Relation'
        return context


class DeleteRelationView(DeleteView):
    template_name = 'employees/all_relations.html'

    def post(self, request, pk):
        qs = Relationship.objects.filter(id=pk)
        if qs.exists() and qs.count() == 1:
            relation = qs.first()
            relation.delete()
            return redirect(reverse('employees:all'))
