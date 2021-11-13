from django.db.models import query
from rest_framework import serializers, viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated , IsAdminUser , AllowAny , BasePermission
from rest_framework.views import APIView
from .serializers import FactorySerializer, ShopfloorSerializer, ProductLineSerializer, SensorTypeSerializer, SensorSerializer, ProductSubLineSerializer
from .models import Factory, ProductLine, Sensor, SensorType, ShopFloor, ProductSubLine
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.response import Response
import requests
from django.shortcuts import get_object_or_404
import json



class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
            # return True
        return request.user==obj.owner or request.user.is_superuser
        


class FactoryViewSet (viewsets.ModelViewSet):
    # permission_classes = [IsOwnerOrAdmin]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()

    def list(self,request):
        qset = Factory.objects.filter(owner = request.user.id)
        serializer = FactorySerializer(instance=qset, many=True)
        return Response(serializer.data)

class ShopfloorViewSet (viewsets.ModelViewSet):
    serializer_class = ShopfloorSerializer
    queryset = ShopFloor.objects.all()


class ProductlineViewSet (viewsets.ModelViewSet):
    serializer_class = ProductLineSerializer
    queryset = ProductLine.objects.all()
    

class ProductSubLineViewSet (viewsets.ModelViewSet):
    serializer_class = ProductSubLineSerializer
    queryset = ProductSubLine.objects.all()


class SensorTypeViewSet (viewsets.ModelViewSet):
    serializer_class = SensorTypeSerializer
    queryset = SensorType.objects.all()


class SensorViewSet (viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()



class SubLinesAPIView(generics.RetrieveAPIView):
    # queryset = ProductSubLine.objects.all()
    # serializer_class = ProductSubLineSerializer
    def retrieve(self, *args, **kwargs):
        owner = self.kwargs['owner_id']
        lineSublines = ProductSubLine.objects.filter(line_id = owner)
        serializer = ProductSubLineSerializer(lineSublines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductlineApiView (generics.RetrieveAPIView):
    # serializer_class = ProductLineSerializer
    # queryset = ProductLine.objects.all()

    def retrieve(self, *args, **kwargs):
        fact_id = self.kwargs['fact_id']
        qset = ProductLine.objects.filter(factory_id = fact_id)
        serializer = ProductLineSerializer(instance=qset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
