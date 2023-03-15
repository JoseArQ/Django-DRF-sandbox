from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from trivia.models import Question, Level
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

    def post(self, request, format=None):
        data = request.data
        question = data.get('question', '')
        level_id = data.get('level_id', None)

        response = {}
        if not question:
            response = {
                "success": False,
                "error": "Invalid question"
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(question, str):
            response = {
                "success": False,
                "error": "Invalid question data type. Must be a string value"
            } 
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        if level_id is None:
            response = {
                "succes": False,
                "error": "level id not found",
            } 
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            level = Level.objects.get(id=level_id)
            print(level.level)
            new_question = Question.objects.create(
                question=question,
                level=level
            )
            print(f"new question: {new_question}")
            response = {
                "succes": True,
                "message": f"create new question succesfully",
            } 
        except Exception as e:
            print(f"error getting level {level_id}: {e}")
            response = {
                "succes": False,
                "error": str(e),
            } 
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            data=response,
            status=status.HTTP_200_OK
            )