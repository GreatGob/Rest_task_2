from django.test import TestCase
from .models import *
from .views import *

# Create your tests here.
class CompanyModelTests(TestCase):
    def test_company_list(self):
        response = self.client.get('companies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], CompanyList)

    def test_company_detail(self):
        response = self.client.get('companies/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], CompanyDetail)

class EmployeeModelTests(TestCase):
    def test_employee_list(self):
        response= self.client.get('companies/1/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], EmployeeList)
    def test_employee_detail(self): 
        response= self.client.get('companies/1/employees/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], EmployeeDetail)
