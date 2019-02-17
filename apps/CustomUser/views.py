from django.shortcuts import render
from django.views.generic.edit import (
	CreateView, UpdateView, DeleteView)
from django.views.generic import ListView, DetailView
from .models import User
from django.contrib.auth import get_user_model
from .forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})