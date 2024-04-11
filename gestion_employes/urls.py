"""
URL configuration for gestion_employes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_gestion_employes import views
from app_gestion_employes.views import employee_list
# from app_gestion_employes.views import departement_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('about/', views.about, name='about.html'),
    path('services/', views.services, name='services.html'),
    path('contact/', views.contact, name='contact.html'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/update/', views.employee_update, name='update_employee'),
    path('employees/delete/', views.employee_delete, name='employee_delete'),
    path('employees/details//<int:employee_id>/', views.employee_details, name='employee_details'),
    path('departments/', views.department_list, name='department_list'),
    # path('departments/create/', views.department_create, name='department_create'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('departments/<int:pk>/update/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),
]
    
