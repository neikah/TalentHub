from role_required import group_required
from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

@group_required("Recruiter", "Admin", "Candidate")
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')

    return render(request, 'recruitment/job_list.html', {
        'jobs': jobs
    })


@group_required("Recruiter", "Admin")
def add_job(request):


    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('job_list')

    else:

        form = JobForm()

    return render(request, 'recruitment/add_job.html', {
        'form': form
    })