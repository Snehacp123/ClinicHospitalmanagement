# appointments/views.py

from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, Admin ,Department,Doctor
from .forms import AppointmentForm, AdminForm,DepartmentForm,DoctorForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


# @login_required(login_url='/login/')
def appointment_form(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Add validation for overlapping appointments and clinic working hours
            appointment = form.save(commit=False)
            appointment.status = "pending"
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

@login_required(login_url='/login/')
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

# Super Admin Only Views
# @login_required(login_url='/login/')
def admin_list(request):
    # if not request.user.is_superuser:
    #     return redirect('')  # Redirect non-superusers to login page

    admins = Admin.objects.all()
    return render(request, 'admin_list.html', {'admins': admins})

# @login_required(login_url='/login/')
def create_admin(request):
    # if not request.user.is_superuser:
    #     return redirect('login')  # Redirect non-superusers to login page

    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            user = form.cleaned_data.get('user')
            admin.user = user
            admin.save()
            return redirect('admin_list')
    else:
        form = AdminForm()
    return render(request, 'create_admin.html', {'form': form})



def create_Department(request):
    # if not request.user.is_superuser:
    #     return redirect('login')  # Redirect non-superusers to login page

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            user = form.cleaned_data.get('user')
            admin.user = user
            admin.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'create_Department.html', {'form': form})



def index(request):

    return render(request,"index.html")

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def rename_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'rename_department.html', {'form': form})

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'delete_department.html', {'department': department})


def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    doctors = Doctor.objects.filter(department=department)
    return render(request, 'department_detail.html', {'department': department, 'doctors': doctors})

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DoctorForm()
    return render(request, 'create_doctor.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        
    return render(request, 'login.html')


def registration_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=email, email=email, password=password)
        # You can add more user-related fields here
        
        return redirect('login')
    
    return render(request, 'registration.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        
        # Generate and send password reset link with token
        token = default_token_generator.make_token(user)
        reset_link = f'http://yourdomain.com/reset-password/{user.pk}/{token}/'
        
        send_mail(
            'Password Reset',
            f'Click the following link to reset your password: {reset_link}',
            'from@example.com',
            [email],
            fail_silently=False,
        )
        
    return render(request, 'forgot_password.html')