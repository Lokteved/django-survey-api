from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Survey
from .serializers import SurveySerializer
from datetime import datetime, timezone


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.filter(expires_at__gt=datetime.now(timezone.utc))
    serializer_class = SurveySerializer

