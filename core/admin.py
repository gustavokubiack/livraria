from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Autor, Categoria, Editora, Livro, Usuario

# from faker import Faker



@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")
    list_filter = ("nome",)
    ordering = ("nome", "email")
    actions = ['gerar_autores']

    # def gerar_autores(self, request, queryset):
    #     faker = Faker()
    #     for _ in range(10):
    #         Autor.objects.create(
    #             nome=faker.name(),
    #             email=faker.email(),
    #         )
    #     self.message_user(request, 'Autores gerados com sucesso!')
    # gerar_autores.short_description = 'Gerar autores'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("descricao",)
    search_fields = ("descricao",)
    list_filter = ("descricao",)
    ordering = ("descricao",)


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nome",)
    ordering = ("nome",)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "editora", "categoria")
    search_fields = ("titulo", "editora__nome", "categoria__descricao")
    list_filter = ("editora", "categoria")
    ordering = ("titulo", "editora", "categoria")
    list_per_page = 25


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "foto",
                    "email",
                    "cpf",
                    "telefone",
                    "data_nascimento",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
