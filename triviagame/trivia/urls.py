from django.urls import path, include
from rest_framework import routers
from trivia.viewsets.level_views import LevelViewSet
from trivia.viewsets.question_views import QuestionApiView

router = routers.DefaultRouter()
router.register(r'levels', LevelViewSet, 'levels')
# router.register(r'questions', QuestionApiView, 'questions')

urlpatterns = router.urls
urlpatterns += [
    path("questions/", QuestionApiView.as_view(), name="questions"),
]