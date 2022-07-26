from django.db import models
from django.utils import timezone
import datetime

# Create your models here
class Company(models.Model):
    __tablename__ = 'company'
    name = models.CharField(max_length=100)
    created= models.DateTimeField('created')

    def __str__(self):
        return self.name
    def published(self):
        now= timezone.now()
        return now-datetime.timedelta(days=1) <= self.created <= now

class Employee(models.Model):
    __tablename__ = 'employee'
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='employee', on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)   
    created = models.DateTimeField('created')

    def __str__(self):
        return f"Name: {self.name} -- Email: {self.email}"
    def published(self):
        now= timezone.now()
        return now-datetime.timedelta(days=1) <= self.created <= now

class Field(models.Model):
    __tablename__ = 'field'
    employee = models.ForeignKey(Employee, related_name='field', on_delete=models.CASCADE)
    first_name= models.CharField(max_length=255, blank=True)
    last_name= models.CharField(max_length=255, blank=True)
    age= models.IntegerField(default=None)
    city= models.CharField(max_length=255, blank=True)
    phone_number= models.ImageField(max_length=255, blank=True)
    created= models.DateTimeField('created')

    def __str__(self):
        return f"{self.first_name} + ' ' + {self.last_name}+' '+ {self.age} + ' ' + {self.phone_number}+' '+ {self.city}"
    def published(self):
        now= timezone.now()
        return now-datetime.timedelta(days=1) <= self.created <= now