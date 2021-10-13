from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout', logout_user, name='logout_user'),
    path('profile', profile, name='profile'),
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('editar/<int:pk>', editar_cliente, name='editar_cliente'),

]
