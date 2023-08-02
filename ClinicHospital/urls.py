
from django.contrib import admin
from django.urls import path
from clinic import views
from  clinic.views   import login_view,registration_view,forgot_password


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create_admin, name='create_admin'),
    path('list/', views.admin_list, name='admin_list'),
    path('index/',views.index, name='index'),

    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('forgot-password/', forgot_password, name='forgot_password'),

    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/new/', views.appointment_form, name='appointment_form'),

    path('departmentcreate', views.create_Department, name='create_department'),
    path('departmentlist', views.department_list, name='department_list'),
    path('rename/<int:pk>/', views.rename_department, name='rename_department'),
    path('delete/<int:pk>/', views.delete_department, name='delete_department'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    path('create-doctor/', views.create_doctor, name='create_doctor'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)