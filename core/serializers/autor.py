from rest_framework.serializers import ModelSerializer, StringRelatedField

from core.models import Autor


class AutorSerializer(ModelSerializer):
    livros = StringRelatedField(many=True)

    class Meta:
        model = Autor
        fields = "__all__"