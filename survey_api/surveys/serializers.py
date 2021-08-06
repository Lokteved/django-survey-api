from django.db import models
from rest_framework import serializers

from .models import Survey, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('type', 'text', 'choices')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'title', 'description', 'created', 'expires_at', 'questions')