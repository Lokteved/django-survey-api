import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Survey, SurveyResponse
from .serializers import SurveySerializer, SurveyResponseSerializer
from datetime import datetime, timezone


class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Survey.objects.filter(expires_at__gt=datetime.now(timezone.utc))
    serializer_class = SurveySerializer


@api_view(['GET'])
def view_responses(request, user_id):
    queryset = SurveyResponse.objects.filter(respondent__auto_id=user_id)
    serializer = SurveyResponseSerializer(queryset, many=True)
    return Response(serializer.data)


api_view(['POST'])
def respond(request, survey_id):
    serializer = SurveyResponseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
