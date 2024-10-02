from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department, Achievement, AchievementEmployee
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm
from django.contrib import messages

def index(request):
    return render(request, "index.html")

@login_required

def employee_list(request):
    employees = Employee.objects.all()
    employee_information = []

    for item in employees:
        temp = []
        temp.append(item)
        achievements = AchievementEmployee.objects.filter(employee=item)
        span = ""
        
        if achievements.exists():
            for iterator in achievements:
                span += f'<span class="badge rounded-pill bg-info text-dark">{iterator.achievement.name}</span>'

        else:
            span = f'<span class="badge rounded-pill bg-danger text-dark">Nothing</span>'

        temp.append(span)
        employee_information.append(temp)

    context = {
        'employee_information' : employee_information
    }

    return render(request, "employee_app/list.html", context)

@login_required

def add_employee(request):
    forms = EmployeeForm()
    
    if request.method == 'POST':
        forms = EmployeeForm(request.POST)
        
        if forms.is_valid():            
            employee = forms.save(commit=False)
            employee.save()
            
            for achievement in forms.cleaned_data['achievements']:
                AchievementEmployee.objects.create(employee=employee, achievement=achievement)

            messages.success(request, 'Employee is added')            
            return redirect('employee_list')
        
    context = {
        'forms' : forms
    }        

    return render(request, 'employee_app/add.html', context)

@login_required

def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee, employee_instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee, employee_instance=employee)

        if form.is_valid():
            form.save()
            AchievementEmployee.objects.filter(employee=employee).delete()
            
            for achievement in form.cleaned_data['achievements']:
                AchievementEmployee.objects.create(employee=employee, achievement=achievement)

            messages.success(request, 'Employee is updated')
            return redirect('employee_list')

    context = {
        'forms': form
    }

    return render(request, 'employee_app/update.html', context)

@login_required

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    AchievementEmployee.objects.filter(employee=employee).delete()
    employee.delete()
    messages.success(request, 'Employee is deleted')
    return redirect('employee_list')
