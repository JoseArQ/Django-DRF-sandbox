
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from trivia.models import Level
from trivia.serializers.level_serializer import LevelSerializer


class LevelViewSet(viewsets.ViewSet):
    """
        viewset for listing levels
    """

    def list(self, request):
        levels = Level.objects.all()
        levels_serealize = LevelSerializer(levels, many=True)

        return Response(data=levels_serealize.data)