from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})

@login_required

def profile(request):
    return render(request, 'profiles/profile.html')

def home(request):
    return render(request, 'profiles/home.html')

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')