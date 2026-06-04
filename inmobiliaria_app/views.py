from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, authenticate, login
from inmobiliaria_app.models import Usuario, Inmueble, Usuario_Inmueble, Comuna, Provincia, Region, Image
from django.contrib import messages
from inmobiliaria_app.forms import LoginForm, CustomUserCreationForm

# Create your views here.

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages = f'Hello {user.username}! You have been logged in'
                return render(request, "mensaje/mensaje.html", {"mensaje":"Gracias por contactarse con nosotros"})
            else:
                message = 'Login failed!'
                return render( {message})
    return render(request, "login.html", {'form':form, 'title':'log in'})

def salir(request):
    logout(request)
    return redirect('/')

def register(request):
    data = {"form": CustomUserCreationForm()}
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request,user)
            return render(request, "mensaje/mensaje.html", {"mensaje":"Gracias por registrarte a OnlyFlans"})
    return render(request, "register.html", data)

def home(request):
    inmuebles = Inmueble.objects.filter(activo=True)
    return render(request=request, template_name='home.html', context={'inmuebles':inmuebles})
