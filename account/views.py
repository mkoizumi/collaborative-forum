from django.shortcuts import render
from django.urls import reverse_lazy
from account import forms
from django.views.generic import CreateView

# Create your views here.
class Register(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')  # sign up then it will take user to login.html
    template_name = 'account/register.html'
