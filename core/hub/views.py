from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.decorators import login_required  
from .models import Project  

@login_required  
def home(request):  
    # Filter projects by the current user  
    projects = Project.objects.filter(user=request.user)  
    return render(request, 'hub/home.html', {'projects': projects})  

def signup(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('login')  # Redirect to login page after signup  
    else:  
        form = UserCreationForm()  
    return render(request, 'hub/signup.html', {'form': form})  