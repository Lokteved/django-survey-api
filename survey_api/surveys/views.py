from rest_framework import viewsets
from .models import Survey, SurveyResponse
from .serializers import SurveySerializer, SurveyResponseSerializar
from datetime import datetime, timezone


class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Survey.objects.filter(expires_at__gt=datetime.now(timezone.utc))
    serializer_class = SurveySerializer


class SurveyResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializar

    # def get_queryset(self):
    #     queryset = Response.objects.filter(user_id=self.kwargs.get('user_id'))

