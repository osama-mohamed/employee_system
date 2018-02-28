from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from .forms import (
    AddEmployeeForm,
    UpdateEmployeeForm,
    AddRelationForm,
    UpdateSalaryForm,
)
from .models import Employees, Relationship


# show all employees
class AllEmployeesView(ListView):
    template_name = 'employees/all_employees.html'
    # template_name = 'employees/all_employees_table.html'

    def get_queryset(self):
        qs = Employees.objects.filter(activated=True).order_by('-id')
        return qs

    def get_context_data(self, **kwargs):
        context = super(AllEmployeesView, self).get_context_data(**kwargs)
        context['title'] = 'All Employees'
        return context


# show employee detail
class EmployeeDetailView(DetailView):
    template_name = 'employees/employee_detail.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'], activated=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee'
        return context


# add new employee
class AddEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'employees/add_new_employee.html'

    def get_context_data(self, **kwargs):
        context = super(AddEmployeeView, self).get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        return context


# update employee information except salary
class EmployeeUpdateView(UpdateView):
    form_class = UpdateEmployeeForm
    model = Employees
    template_name = 'employees/employee_update.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'], activated=True, freeze=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Employee'
        return context


# update employee salary, deduction and earning
class SalaryUpdateView(UpdateView):
    form_class = UpdateSalaryForm
    model = Employees
    template_name = 'employees/update_employee_salary.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'], activated=True, freeze=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super(SalaryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Salary'
        qs = Employees.objects.filter(id=self.kwargs['pk'], activated=True, freeze=False).first()
        context['name'] = qs.full_name
        context['id'] = qs.id
        return context


# delete employee if not connected to a job
class EmployeeDeleteView(DeleteView):
    template_name = 'employees/employee_detail.html'

    def post(self, *args, **kwargs):
        qs = Employees.objects.filter(id=self.kwargs['pk'], freeze=False).first()
        job_status = qs.job
        if job_status is None or job_status == '':
            qs.delete()
            return redirect(reverse('employees:all'))
        else:
            qs.freeze = True
            qs.save()
            messages.error(self.request, 'you can not delete this employee because he has a job')
            return redirect(reverse('employees:all'))


# show all relations for married employees
class AllRelationsView(ListView):
    template_name = 'employees/all_relations.html'

    def get_queryset(self):
        qs = Relationship.objects.filter(employee_id=self.kwargs['pk']).order_by('-id')
        return qs

    def get_context_data(self, **kwargs):
        context = super(AllRelationsView, self).get_context_data(**kwargs)
        context['title'] = 'All Relations'
        context['name'] = Employees.objects.filter(id=self.kwargs['pk']).first().full_name
        context['id'] = Employees.objects.filter(id=self.kwargs['pk']).first().id
        return context


# add relation to married employees
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
            qs = Employees.objects.filter(id=pk, activated=True, freeze=False).first()
            relation = Relationship.objects.create(
                employee=qs,
                relationship_type=form.cleaned_data.get('relationship_type'),
                name=form.cleaned_data.get('name'),
                age=form.cleaned_data.get('age'),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
            )
            return redirect(reverse('employees:all-relations', kwargs={'pk': pk}))
        else:
            messages.error(request, 'you can not add relation to this employee')
            context = {
                'form': form,
                'title': 'Add Relation'
            }
            return render(request, self.template_name, context)


# update relation for married employees
class UpdateRelationView(UpdateView):
    form_class = AddRelationForm
    model = Relationship
    template_name = 'employees/update_relation.html'

    def get_success_url(self):
        employee_id = Relationship.objects.filter(id=self.kwargs['pk']).first().employee_id
        return reverse_lazy('employees:all-relations', kwargs={'pk': employee_id})

    def get_queryset(self):
        qs = Relationship.objects.filter(id=self.kwargs['pk'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(UpdateRelationView, self).get_context_data(**kwargs)
        context['title'] = 'Update Relation'
        return context


# delete relation from married employees
class DeleteRelationView(DeleteView):
    queryset = Relationship.objects.all()
    template_name = 'employees/all_relations.html'

    def get_success_url(self):
        employee_id = Relationship.objects.filter(id=self.kwargs['pk']).first().employee_id
        return reverse_lazy('employees:all-relations', kwargs={'pk': employee_id})
