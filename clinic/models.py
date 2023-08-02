
from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
   

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    place = models.CharField(max_length=100)
    date = models.DateField()
    time_slot = models.TimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")])
    admin_approval = models.ForeignKey(Admin, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    



class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
    qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.name