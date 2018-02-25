from django import forms
from .models import Employees


class AddEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(
        attrs={
            'placeholder': 'First name',
            'class': 'form-control',
        }))
    middle_name = forms.CharField(label='Middle name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Middle name',
            'class': 'form-control',
        }))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Last name',
            'class': 'form-control',
        }))
    full_name = forms.CharField(label='Full name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Full name',
            'class': 'form-control',
        }))
    national_identifier = forms.CharField(label='National Identifier', widget=forms.TextInput(
        attrs={
            'placeholder': 'National Identifier',
            'class': 'form-control',
        }))
    age = forms.CharField(label='Age', widget=forms.TextInput(
        attrs={
            'placeholder': 'Age',
            'class': 'form-control',
        }))
    place_of_birth = forms.CharField(label='Place Of Birth', widget=forms.TextInput(
        attrs={
            'placeholder': 'Place Of Birth',
            'class': 'form-control',
        }))
    job = forms.CharField(label='Job', widget=forms.TextInput(
        attrs={
            'placeholder': 'Job',
            'class': 'form-control',
        }))
    country = forms.CharField(label='Country', widget=forms.TextInput(
        attrs={
            'placeholder': 'Country',
            'class': 'form-control',
        }))
    nationality = forms.CharField(label='Nationality', widget=forms.TextInput(
        attrs={
            'placeholder': 'Nationality',
            'class': 'form-control',
        }))
    salary = forms.CharField(label='Salary', widget=forms.TextInput(
        attrs={
            'placeholder': 'Salary',
            'class': 'form-control',
        }))

    class Meta:
        model = Employees
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'full_name',
            'national_identifier',
            'age',
            'gender',
            'date_of_birth',
            'place_of_birth',
            'position',
            'job',
            'country',
            'nationality',
            'marital_status',
            'salary',
        ]

    def clean_national_identifier(self):
        national_identifier = self.cleaned_data.get('national_identifier')
        qs = Employees.objects.filter(national_identifier__iexact=national_identifier)
        if qs.exists():
            raise forms.ValidationError('This Employee is already Added before!')
        return national_identifier
