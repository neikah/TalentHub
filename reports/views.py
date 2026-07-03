from django.shortcuts import render

from employees.models import Employee
from recruitment.models import Job
from attendance.models import Attendance
from leave_management.models import Leave


def report_dashboard(request):

    context = {

        'employees': Employee.objects.all(),

        'jobs': Job.objects.all(),

        'attendance': Attendance.objects.all(),

        'leaves': Leave.objects.all(),

    }

    return render(request,'reports/report_dashboard.html',context)