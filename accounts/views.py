from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import User
from .forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success')
            return redirect('view_account', user.pk)
        else:
            messages.error(request, 'ERROR')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Success Login')
            return redirect('view_account', user.pk)
        else:
            messages.error(request, 'ERROR')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


class ViewUser(DeleteView):
    model = User
    template_name = 'accounts/account_user.html'
    context_object_name = 'user'
    pk_url_kwarg = 'pk'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

