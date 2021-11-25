from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from factory.serializers import SensorSerializer
from factory.models import Factory, ProductLine, Sensor, SensorType, ShopFloor, ProductSubLine
from rest_framework import status, generics
from rest_framework.response import Response
from django.forms.models import model_to_dict
import requests
import traceback
from .gatewayApis import inlocal_local_getLogs, inlocal_server_getLogs, inserver_getLogs
from .gatewayApis import inlocal_server_live, inlocal_local_live, inserver_live



def cal_aggr(start_time, end_time, dur_time):

    URL = inlocal_local_getLogs()
    BODY ={
            "start_time": start_time,
            "end_time": end_time,
            "dur_time": dur_time
        }
    logs_aggregated = requests.post(url = URL, data = BODY)
    print("body:",BODY)
    print("url",URL)
    print("logs return data:", logs_aggregated)
    data = logs_aggregated.json()

    return data

# class LineSensorsAggrAPIView(generics.RetrieveAPIView):
#     def retrieve(self, request, *args, **kwargs):
        # owner = self.kwargs['owner_id']

@api_view(['POST'])
def sensorsAggrData(request):
    if request.method == 'POST':        
        if ('start_time' in request.data) and ('end_time' in request.data) and ('dur_time' in request.data):
            if (request.data['start_time'] and request.data['end_time'] and request.data['dur_time']):      
                try:
                    sensorInLines = Sensor.objects.all()
                    response = []
                    live_datas = cal_aggr(request.data['start_time'], request.data['end_time'], request.data['dur_time'])
                    for sensor in sensorInLines:
                        # print(model_to_dict(sensor)['subline_id'])
                        # s_id = sensor.subline_id
                        # print(s_id.id)
                        # subline = ProductSubLine.objects.get(id=(sensor.subline_id).id)
                        # print(subline)
                        line = ProductLine.objects.get(id=(sensor.line_id).id)
                        # print(line)
                        floor = ShopFloor.objects.get(id=(line.floor_id).id)
                        # print(floor)
                        factory = Factory.objects.get(id=(floor.factory_id).id)
                        # print(factory)

                        mac = sensor.mac_addr
                        pin = sensor.port
                        sensor_data = 0.0
                        sensor_timed_data = []
                        time = 0
                        for timeseperated_data in live_datas: 
                            if timeseperated_data:
                                for gateway_data in timeseperated_data:
                                    if gateway_data['mac_addr'] == mac and gateway_data['pin'] == pin:    
                                        if(gateway_data['sum_of_diff'] < 0 ):
                                            sensor_timed_data.append({"time":time, "value":"no data"})

                                        else:   
                                            sensor_data = sensor_data + gateway_data['sum_of_diff']
                                            sensor_timed_data.append({"time":time, "value":gateway_data['sum_of_diff']})
                                            # sensor_timed_data[str(time)] = gateway_data['sum_of_diff']
                            time = time + 1
                                        
                        # print("factory_id",factory.id)
                        # print("line_id",line.id)
                        resJsoned = {"aggr_data": sensor_data, "data_in_time": sensor_timed_data}
                        resJsoned.update(SensorSerializer(sensor).data)
                        resJsoned.update({"factory_id":factory.id})
                        response.append((resJsoned))
                    return Response((response), status=status.HTTP_200_OK)
                except Sensor.DoesNotExist:
                    return Response({"detail": "Sensor Not found."}, status=status.HTTP_404_NOT_FOUND)
                except :
                    traceback.print_exc()
                    return Response({"problem"}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({"no time specified"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"no time specified"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def lineSensorsAggr(request):
    if request.method == 'POST':        
        if ('start_time' in request.data) and ('end_time' in request.data) and ('dur_time' in request.data) and ('line_id' in request.data):
            if (request.data['start_time'] and request.data['end_time'] and request.data['dur_time']) and request.data['line_id']:      
                try:
                
                    sensorInLines = Sensor.objects.filter(line_id = request.data['line_id'])
                    response = []
                    live_datas = cal_aggr(request.data['start_time'], request.data['end_time'], request.data['dur_time'])
                    for sensor in sensorInLines:
                        
                        line = ProductLine.objects.get(id=(sensor.line_id).id)
                        # print(line)
                        floor = ShopFloor.objects.get(id=(line.floor_id).id)
                        # print(floor)
                        factory = Factory.objects.get(id=(floor.factory_id).id)
                        # print(factory)

                        mac = sensor.mac_addr
                        pin = sensor.port
                        sensor_data = 0.0
                        sensor_timed_data = []
                        time = 0
                        # print("time seperated dataaaaaaaaaaaaaaa", live_datas )
                        for timeseperated_data in live_datas: 
                            if timeseperated_data:
                                sensorInFlag =False
                                for gateway_data in timeseperated_data:
                                    if gateway_data['mac_addr'] == mac and gateway_data['pin'] == pin:    
                                        sensorInFlag = True
                                        if(gateway_data['sum_of_diff'] < 0 ):
                                            sensor_timed_data.append({"x":time, "y":-1})

                                        else:   
                                            # sensor_data = sensor_data + gateway_data['sum_of_diff']
                                            sensor_timed_data.append({"x":time, "y":gateway_data['sum_of_diff']})
                                            # sensor_timed_data[str(time)] = gateway_data['sum_of_diff']
                                if not (sensorInFlag):
                                    sensor_timed_data.append({"x":time, "y":-1})
                            else: 
                                sensor_timed_data.append({"x":time, "y":-1})
                            time = time + 1
                                        
                        # print("factory_id",factory.id)
                        # print("line_id",line.id)
                        resJsoned = {"id": sensor.name , "data": sensor_timed_data}
                        # resJsoned.update(SensorSerializer(sensor).data)
                        # resJsoned.update({"factory_id":factory.id, "line_id":line.id})
                        response.append((resJsoned))
                    return Response((response), status=status.HTTP_200_OK)
                except Sensor.DoesNotExist:
                    return Response({"detail": "Sensor Not found."}, status=status.HTTP_404_NOT_FOUND)
                except :
                    traceback.print_exc()
                    return Response({"problem"}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({"period time or line id is not specified"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"period time or line id is not specified"},status=status.HTTP_400_BAD_REQUEST)


