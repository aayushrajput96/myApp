from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

def home(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'home.html')

    return render(request, 'home.html')

def login_view(request):
    if request.method != "POST":
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        messages.error(request, 'Please enter both username and password')
        return redirect('/login/')

    user = authenticate(username=username, password=password)

    if user is None:
        messages.error(request, 'Invalid username or password')
        return redirect('/login/')

    auth.login(request, user) 

    messages.success(request, 'Login successful')
    return redirect('/dashboard/')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Log in the user after successful signup
            auth.login(request, user)
            # Redirect to the dashboard or another page upon successful signup
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    # Authentication middleware ensures only authenticated users can access this view
    return render(request, 'dashboard.html')
