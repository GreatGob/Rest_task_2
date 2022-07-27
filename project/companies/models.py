from django.db import models
from django.utils import timezone
import datetime

# Create your models here
class Company(models.Model):

    name = models.CharField(max_length=100)
    located= models.CharField(max_length=100)
    descriptions=models.TextField(blank=True, max_length=100)
    created= models.DateTimeField('created')

    def __str__(self):
        return self.name
    def published(self):
        now= timezone.now()
        return now-datetime.timedelta(days=1) <= self.created <= now

class Employee(models.Model):

    company = models.ForeignKey(Company, related_name='employee', on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=100)   

    full_name= models.CharField(max_length=255, blank=True)
    age= models.IntegerField(default=None)
    city= models.CharField(max_length=255, blank=True)
    phone_number= models.IntegerField(blank=True)
    created= models.DateTimeField('created')
    
    def __str__(self):
        return f"Name: {self.name} -- Email: {self.email}"
    def published(self):
        now= timezone.now()
        return now-datetime.timedelta(days=1) <= self.created <= now   