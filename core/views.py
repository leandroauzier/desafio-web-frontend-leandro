from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from core.forms import ClienteForm
from core.models import Cliente
from setup import settings


def home(request, template_name="home.html"):
    return render(request, template_name)


def login_user(request, template_name="account/login.html"):
    next = request.GET.get('next', '/accounts/profile')

    if request.user.is_authenticated:
        return redirect('core:profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active == 'False':
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                login(request, user)
                return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    return render(request, template_name, {'redirect_to': next})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


@login_required
def profile(request, template_name="account/profile.html"):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }

    return render(request, template_name, context)

@login_required
def cadastrar_cliente(request, template_name="listar.html"):
    if request.method == "POST":
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('core:profile')

    else:
        form = ClienteForm()

    return render(request, template_name, {'form': form})

@login_required
def editar_cliente(request, pk, template_name="listar.html"):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('core:profile')

    else:
        form = ClienteForm(instance=cliente)

    return render(request, template_name, {'form': form})


def filtrar(request):
    if request.is_ajax():
        status = request.POST.get('status')
        renda = request.POST.get('renda')


        if renda:
            if not status:
                clientes = Cliente.objects.filter(
                    renda=renda
                )
            else:
                clientes = Cliente.objects.filter(
                    status=status,
                    renda=renda
                )

        if status:
            if not renda:
                clientes = Cliente.objects.filter(
                    status=status,
                )
            else:
                clientes = Cliente.objects.filter(
                    status=status,
                    renda=renda
                )

        clientes = Cliente.objects.filter(
            status = status
        )

        return JsonResponse({'data':clientes})
    return JsonResponse({})

