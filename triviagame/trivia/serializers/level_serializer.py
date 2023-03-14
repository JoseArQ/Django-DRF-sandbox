from rest_framework import serializers
from trivia.models import Level

class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'
        read_only_fields = ('id', 'level', 'score',)