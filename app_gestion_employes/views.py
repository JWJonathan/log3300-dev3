from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.
# from .models import Department
from app_gestion_employes.models import Employees
from app_gestion_employes.forms import EmployeeForm  # Si vous utilisez un formulaire Django


def home_page(request):
    # employees = Employees.objects.all()
    return render(request, 'homepage.html')

def about(request):
    # employees = Employees.objects.all()
    return render(request, 'about.html')

def services(request):
    # employees = Employees.objects.all()
    return render(request, 'services.html')

def contact(request):
    # employees = Employees.objects.all()
    return render(request, 'contact.html')

def employee_list(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def employee_details(request, employee_id):
    employee = get_object_or_404(Employees, employee_id=employee_id)
    context = {
        'employee': employee,
    }
    return render(request, 'employee_detail.html', context)



def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Sauvegarde du formulaire mais sans commiter à la base de données
            employee = form.save(commit=False)
            # Maintenant, nous pouvons accéder au champ du département dans le formulaire
            department_name = form.cleaned_data['department_name']
            # Assigner le nom du département à l'employé
            employee.department_name = department_name
            # Enregistrer l'employé avec le département attribué
            employee.save()
            return redirect('employee_list')  # Redirige vers la liste des employés après la création réussie
    else:
        form = EmployeeForm()
    return render(request, 'employee_create.html', {'form': form})


def employee_update(request):
    employees = Employees.objects.all()
    return render(request, 'employee_update.html', {'employees': employees})

def employee_delete(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def department_list(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def department_create(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def department_detail(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def department_update(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
def department_delete(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})