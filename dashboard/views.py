from django.shortcuts import render

from recruitment.models import Job
from employees.models import Employee
from attendance.models import Attendance
from leave_management.models import Leave
from notifications.models import Notification


def home(request):

    if not request.user.is_authenticated:
        return render(request,"home.html")

    return render(request,"dashboard/home.html")

    jobs = Job.objects.all()

    employees = Employee.objects.all()

    attendance = Attendance.objects.all()

    leaves = Leave.objects.all()

    notifications = Notification.objects.order_by('-created_at')[:5]

    context = {

        'jobs': jobs.order_by('-created_at'),

        'total_jobs': jobs.count(),

        'total_employees': employees.count(),

        'applications': 0,

        'interviews': 0,

        'leave_requests': leaves.count(),

        'attendance_today': attendance.count(),

        'notifications': notifications,

    }

    return render(
        request,
        'dashboard/home.html',
        context
    )