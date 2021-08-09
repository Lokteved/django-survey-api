from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Answer, Survey, Response, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('type', 'text', 'choices')


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    you_answered = serializers.CharField(source='body')

    class Meta:
        model = Answer
        fields = ('question', 'you_answered')
    
    def get_question(self, obj):
        return obj.question.text



class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', 'title', 'description', 'created', 'expires_at', 'questions')

class ResponseSerializar(serializers.ModelSerializer):
    respondent = serializers.StringRelatedField()
    survey = serializers.StringRelatedField()
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Response
        fields = ('respondent', 'created', 'survey', 'answers')