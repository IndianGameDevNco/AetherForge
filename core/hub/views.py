from rest_framework import generics, permissions
from .serializers import ProjectSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import logout  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.decorators import login_required  
from .models import Project  

@login_required  
def home(request):  
    # Filter projects by the current user  
    projects = Project.objects.filter(user=request.user)  
    return render(request, 'hub/home.html', {'projects': projects})  

def login_view(request):
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

class ProjectListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return projects for the logged-in user
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign user to new projects
        serializer.save(user=self.request.user)

class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)