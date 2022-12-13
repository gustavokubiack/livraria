from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao

    # def __unicode__(self):
    #     return self.descricao