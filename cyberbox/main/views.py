from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from main.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = CreateUserForm()
        context = {
            'form': form,
        }
        return render(request, 'main/sign_up.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account %s was created.' % form.cleaned_data.get('username'))
            return redirect('sign-in')
        context = {
            'form': form,
        }
        return render(request, 'main/sign_up.html', context)


class SignInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'main/sign_in.html', {})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'main/sign_in.html', context)


def SignOutView(request):
    logout(request)
    return redirect('home')


class MainPageView(View):
    def get(self, request):
        return render(request, 'main/index.html')
