from django.contrib.auth.models import AbstractUser
from django.db import models

from uploader.models import Image


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    telefone = models.CharField(max_length=11, blank=True, null=True, unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )