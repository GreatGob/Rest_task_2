from .models import *
from .serializers import *

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class  CompanyList(viewsets.ModelViewSet):
    model= Company
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()

    def create(self, request, *args, **kwargs):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetail(viewsets.ModelViewSet):
    model= Company
    serializer_class= CompanySerializer

    def retrieve(self, pk= None):
        instance= self.get_object()
        return Response(self.serializer_class(instance).data, status= status.HTTP_200_OK)
    
    def update(self, pk= None):
        instance= self.get_object(pk= pk)
        serializer= self.serializer_class(instance= instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk= None):
        instance= self.get_object(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class  EmployeeList(viewsets.ModelViewSet):
    model= Employee
    serializer_class = EmployeeSerializer

    def get_queryset(self, pk=None):
        return Employee.objects.get()

    def create(self, request, *args, **kwargs): 
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(viewsets.ModelViewSet):
    model= Employee
    serializer_class= EmployeeSerializer

    def retrieve(self, pk= None):
        instance= self.get_object()
        return Response(self.serializer_class(instance).data, status= status.HTTP_200_OK)
    
    def update(self, pk= None):
        instance= self.get_object(pk= pk)
        serializer= self.serializer_class(instance= instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk= None):
        instance= self.get_object(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
