
from .serializers import CompanySerializer, EmployeeSerializer, FieldSerializer
from .models import Company, Employee, Field

from rest_framework import status
from rest_framework.response import Response    
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
# Create your views here.

# @api_view()
# def api_root(request, format= None):
#     return Response({
#         'companies': reverse('company-list', request= request, format= format),
#     })

class CompanyList(viewsets.ModelViewSet):
    model= Company
    serializer_class= CompanySerializer

    def get_queryset(self):
        return Company.objects.all()
    

class CompanyDetail(RetrieveUpdateDestroyAPIView):
    model= Company
    serializer_class= CompanySerializer

    def get(self, request, *args, **kwargs):
        company= get_object_or_404(Company, id=kwargs.get('pk'))
        serializer= CompanySerializer(company)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        company=  get_object_or_404(Company, id=kwargs.get('pk'))
        serializer= CompanySerializer(company, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(request.data, status= status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, *args, **kwargs):
        company=  get_object_or_404(Company, id=kwargs.get('pk'))
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeList(ListCreateAPIView):
    model= Employee
    serializer_class= EmployeeSerializer

    def get_queryset(self, company_id):
        list= Company.objects.get(pk=company_id)
        return list.employee.all()

    def create(self, request, *args, **kwargs):
        serializer= EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    model= Employee
    serializer_class= EmployeeSerializer

    def get(self, company_id, request, *args, **kwargs):
        list= Company.objects.get(pk=company_id)
        employee= get_object_or_404(list, id=kwargs.get('pk'))
        serializer= EmployeeSerializer(employee)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, company_id, request, *args, **kwargs):
        list= Company.objects.get(pk=company_id)
        employee= get_object_or_404(list, id=kwargs.get('pk'))
        serializer= EmployeeSerializer(employee, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, company_id, request, *args, **kwargs):
        list= Company.objects.get(pk=company_id)
        employee= get_object_or_404(list, id=kwargs.get('pk'))
        employee.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)