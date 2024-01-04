from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .forms import LoginForm
from .models import Register

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = Register.objects.get(username=username)
                if check_password(password, user.password):
                    # Authentication successful
                    # You can add the logic here for what happens after successful login
                    messages.success(request, 'Login successful!')
                    return redirect('your_redirect_view_name')
                else:
                    # Password is incorrect
                    messages.error(request, 'Invalid password')
            except Register.DoesNotExist:
                # Username not found
                messages.error(request, 'Username not found')
        else:
            # Form is not valid
            messages.error(request, 'Invalid form submission')

    else:
        form = LoginForm()

    return render(request, 'useraccount/login.html', {'form': form})

def home(request):
    return HttpResponse("<h1>home</h1>")