from django.core.exceptions import NON_FIELD_ERRORS
from django.forms.utils import ErrorList
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateUserForm,CreateAddressForm,CreateOrtForm


# Create your views here.
def index(request):
    return render(request, "homepage.html")


def register(request):
    global user,address,ort
    try:
        if request.method == 'POST':
            user = CreateUserForm(request.POST)
            address = CreateAddressForm(request.POST)
            ort = CreateOrtForm(request.POST)
            if user.is_valid() and address.is_valid() and ort.is_valid():
                ort.save()
                address.save()
                user.save()
        user = CreateUserForm()
        address = CreateAddressForm()
        ort = CreateOrtForm()
        context = {'user': user,'address':address,'ort':ort}
        return render(request, 'registration/register.html', context)
    except Exception:
        return render(request, 'homepage.html')

