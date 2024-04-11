from django import forms
from app_gestion_employes.models import Employees
from app_gestion_employes.models import Departments

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        # fields = ['employee_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_title', 'manager',]
        fields = '__all__' 
        # model = Departments
        department_name = forms.CharField(label='Nom du département', max_length=255)
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee_id'].required = True  # Rendre le champ employee_id obligatoire