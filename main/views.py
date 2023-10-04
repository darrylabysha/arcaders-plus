from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import password_validation




@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    num_products = len(products)
    verb = "are" if num_products > 1 else "is"
    pluralize = "s" if num_products > 1 else ""

    last_login = request.COOKIES.get('last_login', 'N/A')

    context = {
        'name': request.user.username,
        'class': 'PBP E',
        'products': products,
        'num_products': num_products,
        'verb': verb,
        'pluralize': pluralize,
        #'last_login': request.COOKIES['last_login'],
        'last_login': last_login,  # Use 'last_login' if it exists, otherwise 'N/A'

    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

class CustomRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form fields or add additional fields here if needed.

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        # Add custom password validation logic here.
        if len(password1) < 8:
            raise forms.ValidationError("Your password must contain at least 8 characters.")
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned_data

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect('main:register')

            # Custom password validations
            if len(password) < 8:
                messages.error(request, "Your password must contain at least 8 characters.")
                return redirect('main:register')

            if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                messages.error(request, "Your password must contain both letters and digits.")
                return redirect('main:register')

            if password.isnumeric():
                messages.error(request, "Your password can't be entirely numeric.")
                return redirect('main:register')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
                return redirect('main:register')
            
            if any(field.lower() in password.lower() for field in [username, 'first_name', 'last_name']):
                messages.error(request, "Your password is too similar to your other personal information.")
                return redirect('main:register')

            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Your account has been successfully created!')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:login')
    
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add":
            product.amount += 1
        elif action == "reduce":
            if product.amount > 0:
                product.amount -= 1
        product.save()

    return HttpResponseRedirect(reverse("main:show_main"))

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product.delete()

    return HttpResponseRedirect(reverse("main:show_main"))

def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
