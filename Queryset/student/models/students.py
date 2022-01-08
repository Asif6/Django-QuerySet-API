from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    rool=models.IntegerField(unique=True, null=False)
    city=models.CharField(max_length=200)
    marks=models.IntegerField(null=False)
    pass_date=models.DateField()