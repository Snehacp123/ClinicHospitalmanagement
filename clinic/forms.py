from django import forms
from .models import Admin,Appointment,Department,Doctor

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'password']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'place', 'date']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'department', 'photo', 'qualification']