from django.contrib import admin
from .models import *
# Register your models here.
class EmployeeInLine(admin.TabularInline):
    model= Employee
    extra= 3 
    
class CompanyAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields': ['name']}),
        ('Data information', {'fields': ['created'], 'classes':['collapse']}),
    ]

    list_display= ('name', 'located', 'descriptions')
    list_filter= ['created']
    search_fields= ['name']

    inlines= [EmployeeInLine]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)