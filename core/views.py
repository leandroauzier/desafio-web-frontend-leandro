from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')

