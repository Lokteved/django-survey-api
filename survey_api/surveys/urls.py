from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, SurveyResponseViewSet

router = DefaultRouter()
router.register('surveys', SurveyViewSet)
router.register('responses', SurveyResponseViewSet)

urlpatterns = [
    path('', include(router.urls))
]