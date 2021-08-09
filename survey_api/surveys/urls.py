from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, ResponseViewSet

router = DefaultRouter()
router.register('surveys', SurveyViewSet)
router.register('responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls))
]