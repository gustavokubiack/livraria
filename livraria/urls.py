from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from media.router import router as media_router

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"livros", LivroViewSet)
router.register(r"autor", AutorViewSet)


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Token
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Imagens
    path("api/media/", include(media_router.urls)),
    # OPEN API 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # API REST
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
