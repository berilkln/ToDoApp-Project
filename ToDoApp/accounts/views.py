from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/index.html')

#Register Function
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})



#Login Function
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


#Logout Function
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})