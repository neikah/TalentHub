from role_required import group_required
from django.shortcuts import render, redirect
from .models import PerformanceReview
from .forms import PerformanceReviewForm

@group_required("HR Manager", "Admin")
def performance_list(request):
    reviews = PerformanceReview.objects.all().order_by('-review_date')

    return render(
        request,
        'performance/performance_list.html',
        {
            'reviews': reviews
        }
    )
@group_required("HR Manager", "Admin")
def performance_list(request):
    reviews = PerformanceReview.objects.all().order_by('-review_date')

    return render(
        request,
        'performance/performance_list.html',
        {
            'reviews': reviews
        }
    )


def add_review(request):

    if request.method == "POST":

        form = PerformanceReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('performance_list')

    else:
        form = PerformanceReviewForm()

    return render(
        request,
        'performance/add_review.html',
        {
            'form': form
        }
    )