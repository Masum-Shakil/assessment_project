from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def signup(request):
    forms = RegistrationForm()

    if request.method == 'POST':
        forms = RegistrationForm(request.POST)

        if forms.is_valid():

            try:
                user = forms.save()
                messages.success(request, 'Signup is successful')

            except:
                messages.error(request, 'Something is wrong please try again')

            return redirect('signup')

    context = {
        'forms' : forms
    }

    return render(request, 'user_app/signup.html', context)

def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Signin is successful')
                return redirect('employee_list')
            
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('signin')
    
    context = {
        'form' : form
    }

    return render(request, 'user_app/signin.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')