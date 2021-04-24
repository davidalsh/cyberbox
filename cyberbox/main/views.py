from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from main.forms import LoginForm

from django.contrib.auth import authenticate, login


class MainPageView(View):
    def get(self, request):
        return render(request, 'main/index.html')


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'main/sign_in.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'main/sign-in.html', {'form': form})


class SignUpView(View):
    pass
    # def get(self, request):
    #     return render(request, 'main/sign_up.html')