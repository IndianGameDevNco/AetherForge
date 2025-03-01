from django.shortcuts import render, redirect
from django.contrib.auth import logout  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.decorators import login_required  
from .models import Project  

@login_required  
def home(request):  
    # Filter projects by the current user  
    projects = Project.objects.filter(user=request.user)  
    return render(request, 'hub/home.html', {'projects': projects})  

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Create an instance of the authentication form
        if form.is_valid():  # Check if the form is valid
            return redirect('home')  # Redirect to the home page
    else:
        form = AuthenticationForm()  # Create a new instance of the authentication form
    return render(request, 'hub/login.html')

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')  # Redirect to the login page

def signup(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('login')  # Redirect to login page after signup  
    else:  
        form = UserCreationForm()  
    return render(request, 'hub/signup.html', {'form': form})  
