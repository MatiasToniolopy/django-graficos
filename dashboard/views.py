from django.shortcuts import render, redirect
from .models import PaisData, CovidData
from .forms import PaisDataFrom, CovidDataFrom, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required





@login_required
def index(request):
    data = PaisData.objects.all()
    if request.method == 'POST':
        form = PaisDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PaisDataFrom()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def covid(request):
    data = CovidData.objects.all()
    if request.method == 'POST':
        form = CovidDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/covid')
    else:
        form = CovidDataFrom()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/cov.html', context)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
    return render(request, 'registration/registro.html', data)



