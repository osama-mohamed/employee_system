from django.test import TestCase
from django.core.urlresolvers import reverse


class TestCalls(TestCase):

    def test_new_employee(self):
        response = self.client.post(reverse('employees:add'), {
                                    'first_name': 'OSAMAMOHAMED',
                                    'middle_name': 'octocat',
                                    'last_name': 'octocat',
                                    'full_name': 'octocat',
                                    'national_identifier': '123456789101112',
                                    'age': 23,
                                    'gender': 'Male',
                                    'date_of_birth': '1994-10-01',
                                    'place_of_birth': 'Fayoum',
                                    'position': 'Employee',
                                    'job': 'developer',
                                    'country': 'Fayoum',
                                    'nationality': 'Egyptian',
                                    'marital_status': 'Single',
                                    'salary': '5000',
                                    }
                                    )
        self.assertEqual(response.status_code, 200)
        print(response.context)
        # self.assertEqual(len(response.context['user_one']), 9)
        # self.assertEqual(len(response.context['user_one']['login']), 16)
        # self.assertEqual(response.context['user_one']['login'], 'OSAMAMOHAMED1234')
