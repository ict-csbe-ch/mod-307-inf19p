# Create your views here.

from django.shortcuts import render


def index(request):
    return render(request, 'registration/login.html')


def sign_up(request):
    return render(request, 'registration/sign_up.html')
