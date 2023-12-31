from django.db import models

# Create your models here.
class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    registrationNo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
