from django.urls import path, include
from rest_framework.routers import DefaultRouter
from habits.api.viewset import HabitViewSet, CheckInViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'checkins', CheckInViewSet, basename='checkin')

urlpatterns = [
    path('api/habits/', include(router.urls)),
]
