from django.db import models

# Create your models here.
class Admin(models.Model):
    Employee_ID=models.PositiveIntegerField()
    Task_Title=models.CharField(max_length=100)
    Task_Domain=models.CharField(max_length=100)
    Start_Date=models.DateTimeField(null=True,blank=True)
    End_Date=models.DateField(null=True,blank=True)