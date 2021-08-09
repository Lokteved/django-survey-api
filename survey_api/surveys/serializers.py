from django.db import models
from rest_framework import serializers

from .models import Survey, Response


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'title', 'description', 'created', 'expires_at', 'questions')
        depth = 1

class ResponseSerializar(serializers.ModelSerializer):
    pass