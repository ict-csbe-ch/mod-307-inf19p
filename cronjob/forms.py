from django.forms import ModelForm
from django import forms
from cronjob.models import User, Address, Ort


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','firstName','lastName', 'password']

class CreateAddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street','strassenNr','plz']

class CreateOrtForm(ModelForm):
    class Meta:
        model = Ort
        fields = ['plz','name']
