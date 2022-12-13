from rest_framework.serializers import ModelSerializer, RelatedField

from core.models import Categoria

# from core.serializers import LivroSerializer


class CategoriaSerializer(ModelSerializer):
    # livros = LivroSerializer(many=True)
    class Meta:
        model = Categoria
        fields = ("id", "descricao", "livros")
