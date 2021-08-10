from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Answer, Survey, SurveyResponse, Question, Respondent


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('type', 'text', 'choices')


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    you_answered = serializers.CharField(source='body')

    class Meta:
        model = Answer
        fields = ('question', 'type', 'you_answered')
    
    def get_question(self, obj):
        return obj.question.text
    
    def get_type(self, obj):
        return obj.question.type


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', 'title', 'description', 'created', 'expires_at', 'questions')

class SurveyResponseSerializer(serializers.ModelSerializer):
    respondent = serializers.StringRelatedField()
    survey = serializers.StringRelatedField()
    answers = AnswerSerializer(many=True)

    class Meta:
        model = SurveyResponse
        fields = ('respondent', 'created', 'survey', 'answers')
    
    def validate_respondent(self, value):
        if not value:
            r = Respondent.objects.create()
            r.save()
            value = r.auto_id
        return value
