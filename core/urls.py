from django.urls import path
from .views import login, logout
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login', login),
    path('logout', logout),
]
