from django.urls import path, include
from rest_framework import routers
from trivia.viewsets.level_views import LevelViewSet

router = routers.DefaultRouter()
router.register(r'levels', LevelViewSet, 'levels')

urlpatterns = router.urls