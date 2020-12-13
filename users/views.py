from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignupForm
from django.forms import ValidationError


def login_view(request):
    next = request.GET.get('next')
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

        if next:
            return redirect(next)


    context = {
        'login_form': login_form
    }

    return render(request, 'users/login.html', context)


def signup_view(request):
    next = request.GET.get('next')
    signup_form = SignupForm(request.POST or None)

    if signup_form.is_valid():
        user = signup_form.save(commit=False)
        password = signup_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        if user is not None:
            login(request, user)

        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'signup_form': signup_form,
    }

    return render(request, 'users/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
