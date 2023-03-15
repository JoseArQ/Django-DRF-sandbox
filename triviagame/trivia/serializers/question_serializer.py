from rest_framework import serializers
from trivia.models import Question, Level

class LevelListingField(serializers.RelatedField):
    """
    Representation of a level serializer nested
    """
    def to_representation(self, value):
        return {
            "level": value.level,
            "score": value.score
        }

class QuestionSerializer(serializers.ModelSerializer):

    level = LevelListingField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('id', )
        depth = 1