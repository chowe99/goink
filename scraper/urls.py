# scraper/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import scrape_view, AirQualityDataAPIView
router = DefaultRouter()
router.register(r'datasets', DatasetViewSet, basename='dataset')

urlpatterns = [
    path('scrape/', scrape_view, name='scrape'),
    path('api/air-quality/', AirQualityDataAPIView.as_view(), name='air-quality-data'),
]
