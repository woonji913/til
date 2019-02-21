from django.db import models

# Create your models here.
class Student(models.Model):  
    name = models.CharField(max_length=10) 
    email = models.CharField(max_length=25)
    birthday = models.DateTimeField()  
    age = models.IntegerField()
    
    def __str__(self):
    	return f"{self.name}"