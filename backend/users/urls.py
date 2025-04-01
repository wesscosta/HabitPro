
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.viewset import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/users/', include(router.urls)),
]
