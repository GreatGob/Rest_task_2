from django.urls import path, include
from .views import *
#from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

company_list= CompanyList.as_view({
    'get':'list',
    'post':'create',
})

company_detail= CompanyDetail.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})

employee_list= EmployeeList.as_view({
    'get':'list',
    'post':'create',
})

employee_detail= EmployeeDetail.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})

router= routers.DefaultRouter()
#router.register(r'admin', admin, basename='admin')
# router.register(r'companies', CompanyList, basename='companies-list')
# router.register(r'employees', EmployeeList, basename='employees-list')
# router.register(r'companies/company_id', CompanyDetail, basename='companies-detail')
# router.register(r'companies/company_id/employees', EmployeeList, basename='employees-list')
# router.register(r'companies/company_id/employees/employee_id', EmployeeDetail, basename='employees-detail')


urlpatterns=[
    # path('', include(router.urls)),
    path('companies/', company_list),
    path('companies/<int:pk>/', company_detail),
    path('companies/<int:company_id>/employees/', employee_list),
    path('employees/<int:company_id>/employees/<int:id>/', employee_detail),
]