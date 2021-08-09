from rest_framework import viewsets
from .models import Survey, Response
from .serializers import SurveySerializer, ResponseSerializar
from datetime import datetime, timezone


class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Survey.objects.filter(expires_at__gt=datetime.now(timezone.utc))
    serializer_class = SurveySerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializar

    # def get_queryset(self):
    #     queryset = Response.objects.filter(user_id=self.kwargs.get('user_id'))

