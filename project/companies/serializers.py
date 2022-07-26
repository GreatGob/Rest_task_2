from rest_framework import serializers
from companies.models import Company, Employee, Field

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name', 'created']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = ['id','name', 'email', 'created']

class FieldSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Field
        fields = ['id','first_name', 'last_name', 'age', 'city', 'phone_number', 'created']