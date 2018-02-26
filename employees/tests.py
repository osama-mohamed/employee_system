from django.test import TestCase
from django.core.urlresolvers import reverse


class TestCalls(TestCase):

    def test_new_employee(self):
        response = self.client.post(reverse('employees:add'), {
                                    'first_name': 'OSAMAMOHAMED',
                                    'middle_name': 'octocat',
                                    'last_name': 'octocat',
                                    'full_name': 'octocat',
                                    'national_identifier': 123456789101112,
                                    'age': 23,
                                    'gender': [1],
                                    'date_of_birth': '1994-10-01',
                                    'place_of_birth': 'Fayoum',
                                    'position': [1],
                                    'job': 'developer',
                                    'country': 'Fayoum',
                                    'nationality': 'Egyptian',
                                    'marital_status': [1],
                                    'salary': 5000,
                                    }
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/add_new_employee.html')
        self.assertContains(response, 'developer')

