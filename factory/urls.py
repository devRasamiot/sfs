from django.urls import path, include
from .views import FactoryViewSet, ShopfloorViewSet, ProductlineViewSet,  SensorTypeViewSet, SensorViewSet, ProductSubLineViewSet, SubLinesAPIView, ProductlineApiView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('factory', FactoryViewSet, basename='factory')
router.register('shopfloor', ShopfloorViewSet, basename='shopfloor')
router.register('factoryline', ProductlineViewSet, basename='factoryline')
router.register('subline', ProductSubLineViewSet, basename='factorysubline')
router.register('sensortype', SensorTypeViewSet, basename='sensortype')
router.register('sensor', SensorViewSet, basename='sensor')
# 



urlpatterns =[
    
    path('', include(router.urls)),
    path('subline/line/<int:owner_id>/', SubLinesAPIView.as_view()),
    path('factoryline/factory/<int:fact_id>/', ProductlineApiView.as_view())

]


