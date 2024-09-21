from django.contrib import admin
from crud import models
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['ename','esal','eaddr']

admin.site.register(models.Employee,EmployeeAdmin)