
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CompanyList
#from rest_framework.urlpatterns import format_suffix_patterns

app_name= 'companies'
router = SimpleRouter()
router.register(r'', CompanyList, 'companies')

urlpatterns = [
    #path('', views.api_root),
    path('companies/', include(router.urls, "companies")),
    # path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    # path('companies/<int:pk>/employees/', views.EmployeeList.as_view(), name='employee-list'),
    # path('companies/<int:pk>/employees/<int:employee_id>/', views.EmployeeDetail.as_view, name='employee-detail'),
]
#urlpatterns= format_suffix_patterns(urlpatterns)

