from django.shortcuts import render
from django.views.generic import ListView
from .models import User


class Home(ListView):
    model = User
    template_name = 'accounts/account_user.html'
    context_object_name = 'accounts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

