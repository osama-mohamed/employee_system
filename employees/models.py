from django.db import models
from django.core.urlresolvers import reverse


class Employees(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    Position_CHOICES = [
        ('Employee', 'Employee'),
        ('Manager', 'Manager'),
        ('CEO', 'CEO'),
    ]
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=500)
    national_identifier = models.BigIntegerField()
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    position = models.CharField(choices=Position_CHOICES, max_length=25)
    job = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=25)
    salary = models.PositiveIntegerField()
    deduction = models.PositiveIntegerField(null=True)
    earning = models.PositiveIntegerField(null=True)
    activated = models.BooleanField(default=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('employees:detail', kwargs={'pk': self.pk})


class Relationship(models.Model):
    RELATIONSHIP_TYPE_CHOICES = [
        ('wife', 'Wife'),
        ('child', 'Child'),
        ('husband', 'Husband'),
    ]
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    relationship_type = models.CharField(choices=RELATIONSHIP_TYPE_CHOICES, max_length=25)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee
