from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=50, blank=True)
    telefone = models.CharField("Telefone", max_length=50)
    data_nascimento = models.DateField("Data de nascimento", null=True, blank=True)
    renda = models.DecimalField("Renda", decimal_places=2, max_digits=10, blank=True)
    status = models.BooleanField("Status", default=True, blank=False)
