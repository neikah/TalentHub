from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from role_required import group_required
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import RegisterForm

from django.contrib.auth.models import Group




def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password'])

            user.save()

            candidate_group = Group.objects.get(name="Candidate")
            user.groups.add(candidate_group)

            return redirect('login')

        

    else:

        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

        return redirect("/dashboard/")
    return render(request, 'accounts/login.html')


def logout_view(request):

    logout(request)

    return redirect('login')

@login_required
@group_required("Admin")
def user_list(request):

    users = User.objects.all().order_by("username")

    return render(
        request,
        "accounts/user_list.html",
        {
            "users": users
        }
    )

@login_required
@group_required("Admin")
def edit_user(request, user_id):

    user_obj = get_object_or_404(User, id=user_id)

    groups = Group.objects.all()

    if request.method == "POST":

        group_name = request.POST.get("group")

        is_active = request.POST.get("is_active") == "on"

        user_obj.groups.clear()

        if group_name:

            group = Group.objects.get(name=group_name)
            user_obj.groups.add(group)

        user_obj.is_active = is_active
        user_obj.save()

        return redirect("user_list")

    return render(
        request,
        "accounts/edit_user.html",
        {
            "user_obj": user_obj,
            "groups": groups,
        },
    )