from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=200)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome