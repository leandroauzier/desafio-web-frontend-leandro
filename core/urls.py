from django.urls import path
from .views import index, login, logout

urlpatterns = [
    path('', index),
    path('login', login),
    path('logout', logout),
]
