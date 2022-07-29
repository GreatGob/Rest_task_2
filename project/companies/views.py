from .models import *
from .serializers import *

from rest_framework import viewsets, status
#from rest_framework.decorators import action
from rest_framework.response import Response

class  CompanyList(viewsets.ModelViewSet):
    
    serializer_class = CompanySerializer
    queryset= Company.objects.all()
    
    def get_queryset(self):
        return self.queryset

    def create(self, request):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetail(viewsets.ModelViewSet):

    serializer_class= CompanySerializer
    queryset= Company.objects.all()

    # def retrieve(self, request, pk= None):
    #     query_object= self.get_object()
    #     serializer= self.serializer_class(query_object, many=True)
    #     return Response(serializer.data, status= status.HTTP_200_OK)
    
    def update(self, pk= None):
        get_object= self.get_object()
        serializer= self.serializer_class(get_object, many= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk= None):
        get_object= self.get_object(pk=pk)
        get_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class  EmployeeList(viewsets.ModelViewSet):
    
    serializer_class = EmployeeSerializer
    queryset= Employee.objects.all()

    def get_queryset(self, company_id=None):
        return Employee.objects.filter(company_id=company_id)

    def create(self, request): 
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(viewsets.ModelViewSet):
    
    serializer_class= EmployeeSerializer
    queryset= Employee.objects.all()

    def retrieve(self, id= None, company_id=None):
        get_object= Employee.objects.filter(company_id=company_id)
        get_in_object=get_object.filter(id=id)
        return Response(get_in_object, status=status.HTTP_200_OK)
    
    def update(self, id= None):
        instance= self.get_object(id=id)
        serializer= self.serializer_class(instance= instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, id= None):
        instance= self.get_object(id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
