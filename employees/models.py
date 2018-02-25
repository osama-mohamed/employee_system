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
    Positions = models.PositiveIntegerField(choices=Position_CHOICES)
    job = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    marital_status = models.PositiveIntegerField(choices=MARITAL_STATUS_CHOICES)
    salary = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('employees:detail', kwargs={'pk': self.pk})
