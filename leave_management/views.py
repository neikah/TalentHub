from role_required import group_required
from django.shortcuts import render, redirect
from .models import Leave
from .forms import LeaveForm

@group_required("Employee", "HR Manager", "Admin")

def leave_list(request):
    leaves = Leave.objects.all().order_by('-applied_on')

    return render(
        request,
        'leave_management/leave_list.html',
        {
            'leaves': leaves
        }
    )

@group_required("HR Manager", "Employee", "Admin")
def apply_leave(request):

    if request.method == "POST":

        form = LeaveForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('leave_list')

    else:
        form = LeaveForm()

    return render(
        request,
        'leave_management/apply_leave.html',
        {
            'form': form
        }
    )