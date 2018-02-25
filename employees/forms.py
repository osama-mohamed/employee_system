from django import forms
from .models import Employees


class AddEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(
        attrs={
            'placeholder': 'First name',
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
            'Positions',
            'job',
            'country',
            'nationality',
            'marital_status',
            'salary',
        ]
