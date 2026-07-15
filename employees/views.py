from role_required import group_required
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

@group_required("HR Manager", "Admin")
def employee_list(request):
    employees = Employee.objects.all().order_by('-id')

    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })

@group_required("HR Manager", "Admin")
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