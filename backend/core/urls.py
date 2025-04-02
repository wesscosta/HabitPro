from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import  AllowAny, IsAuthenticated


# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="HabitPro API",
        default_version='v1',
        description="API para gerenciamento de hábitos",
    ),
    public=True,
    permission_classes=(AllowAny,),  # Restrição de acesso ao Swagger
)



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Documentação da API
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Rotas da API separadas por módulo
    path('api/habits/', include('habits.urls')),
    path('api/users/', include('users.urls')),
]
