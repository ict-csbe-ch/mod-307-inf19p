from django.core.exceptions import NON_FIELD_ERRORS
from django.forms.utils import ErrorList
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


# Create your views here.
def index(request):
    return render(request, "homepage.html")


def register(request):
    global form
    try:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    except Exception as err:
        errors = form.errors.setdefault(NON_FIELD_ERRORS, ErrorList())
        errors.append(err)
