from django.urls import path, include
from .views import LineSensorsAPIView, SensorsLogDataAPIView
from .sensorsAggrview import lineSensorsAggr, sensorsAggrData


urlpatterns =[
 
    path('sensor/factorysubline/<int:owner_id>/', LineSensorsAPIView.as_view()),
    # path('sensor/aggrdata/', LineSensorsAggrAPIView.as_view()),
    path('sensor/aggrdata/', sensorsAggrData),
    path('sensor/inline/aggrdata/', lineSensorsAggr),
    path('sensors/logdatas/', SensorsLogDataAPIView.as_view())
    
]


