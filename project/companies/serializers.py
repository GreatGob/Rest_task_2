from rest_framework import serializers
from companies.models import Company, Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    company= CompanySerializer(many=True)
    class Meta: 
        model = Employee
        fields = '__all__'
