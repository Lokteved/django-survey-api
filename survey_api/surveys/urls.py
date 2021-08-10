from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, view_responses, respond

router = DefaultRouter()
router.register('surveys', SurveyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('responses/<str:user_id>', view_responses),
    path('surveys,<int:survey_id>/respond', respond)
]