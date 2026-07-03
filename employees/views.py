from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all().order_by('-id')

    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })


def add_employee(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:

        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {
        'form': form
    })