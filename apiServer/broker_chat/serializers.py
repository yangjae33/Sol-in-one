from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['answer','chatbot_id','chatbot_name','accuracy']