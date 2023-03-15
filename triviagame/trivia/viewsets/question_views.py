from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from trivia.models import Question
from trivia.serializers.question_serializer import QuestionSerializer

class QuestionApiView(APIView):
    """
        view to handle question
    """

    def get(self, request, format=None):
        questions = Question.objects.all()
        questions_serializer = QuestionSerializer(questions, many=True)
        return Response(
            data={
                "success": True,
                "data": questions_serializer.data
            },
            status=status.HTTP_200_OK
            )