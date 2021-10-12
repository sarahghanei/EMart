from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CustomUser
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully.', 'success')
                # after login redirect user to home
                return redirect('cart:home')
            else:
                messages.error(request, 'Email or password is wrong.', 'danger')
    else:
        # show the login form to the user
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You logged out successfully', 'success')
    return redirect(reverse('cart:home'))


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.objects.create_user(email=cd['email'], password=cd['password'])
            user.save()
            messages.success(request, 'User registered successfully.', 'success')
            return redirect(reverse('cart:home'))
        else:
            messages.error(request, 'Registration failed.', 'danger')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
