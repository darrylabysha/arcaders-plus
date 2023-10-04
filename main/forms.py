from django.forms import ModelForm
from main.models import Product
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)