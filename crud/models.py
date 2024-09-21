from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=25)
    esal = models.DecimalField(max_digits=10,decimal_places=2)
    eaddr = models.CharField(max_length=100)

    def __str__(self):
        return self.ename
   
