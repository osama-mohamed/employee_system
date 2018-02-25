from django.db import models
from django.core.urlresolvers import reverse


class Employees(models.Model):
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
    ]
    Position_CHOICES = [
        (1, 'Employee'),
        (2, 'Manager'),
        (3, 'CEO'),
    ]
    MARITAL_STATUS_CHOICES = [
        (1, 'Single'),
        (2, 'Married'),
    ]
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=500)
    national_identifier = models.BigIntegerField()
    age = models.PositiveIntegerField()
    gender = models.PositiveIntegerField(choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    position = models.PositiveIntegerField(choices=Position_CHOICES)
    job = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    marital_status = models.PositiveIntegerField(choices=MARITAL_STATUS_CHOICES)
    salary = models.PositiveIntegerField()
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

