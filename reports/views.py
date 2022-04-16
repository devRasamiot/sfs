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
from .gatewayApis import inlocal_local_getLogsData




class LineSensorsAPIView(generics.RetrieveAPIView):
    def retrieve(self, *args, **kwargs):
        owner = self.kwargs['owner_id']
        sensorInLines = Sensor.objects.filter(subline_id = owner)

        response = []
        try:
            live_datas = requests.get(inlocal_local_live())
            live_datas = live_datas.json()
            # print(type(live_datas))
            # print(sensorInLines, type(sensorInLines))
            for sensor in sensorInLines:
                # print("in for")
                mac = sensor.mac_addr
                # print(mac)
                pin = sensor.port
                sensor_data = "no data"
                for gateway_data in live_datas: 
                    # print("in other for")
                    if gateway_data['mac_addr'] == mac and gateway_data['pin'] == pin:
                        sensor_data = gateway_data['sensor_data']
                        if sensor_data == "None":
                            sensor_data = "no data"
                
                # print("sesnsor", SensorSerializer(sensor).data)
                sensorRes = {"live_data": sensor_data}
                sensorRes.update(SensorSerializer(sensor).data)
                # print("eeeeeeeeeeeeeeee", sensorRes)
                response.append((sensorRes))
                # print(response)
            return Response((response), status=status.HTTP_200_OK)
        except:
            traceback.print_exc()
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


def cal_logs(start_time, end_time):

    URL = inlocal_local_getLogsData()
    BODY ={
            "start_time": start_time,
            "end_time": end_time
        }
    logs_datas = requests.post(url = URL, data = BODY)
    print("body:",BODY)
    print("url",URL)
    print("logs return data:", logs_datas)
    data = logs_datas.json()

    return data


class SensorsLogDataAPIView(generics.RetrieveAPIView):
    def retrieve(self,request, *args, **kwargs):
        try:
            sensorInLines = Sensor.objects.filter(line_id = self.request.query_params.get('line_id'))
            response = []
            live_datas = cal_logs(self.request.query_params.get('start_time'), self.request.query_params.get('end_time'))
            # print(sensorInLines)
            # print('*****************************************************************')
            # print(self.request.query_params.get('line_id'))
            for sensor in sensorInLines:
                sensorRes =[]
                mac = sensor.mac_addr
                # print(mac)
                pin = sensor.port
                sensor_data = -1
                # sensorRes.append(SensorSerializer(sensor).data)
                sensorDataRes = []
                # print(len(live_datas))
                for gateway_data in live_datas: 
                    # print("in other for")
                    if gateway_data['mac_addr'] == mac and gateway_data['pin'] == pin:
                        if sensor_data == "None":
                            sensor_data = -1
                        else:
                            sensor_data = gateway_data['sensor_data']
                        
                        sensorDataRes.append({"x":gateway_data['sendDataTime'], "y":sensor_data})
                        # print("sesnsor", SensorSerializer(sensor).data)
                sensorRes=[{"id": sensor.name , "data": sensorDataRes}]
                # sensorRes.append(sensorDataRes)
                response.append((sensorRes))
            return Response((response), status=status.HTTP_200_OK)
        except Sensor.DoesNotExist:
            return Response({"detail": "Sensor Not found."}, status=status.HTTP_404_NOT_FOUND)
        except :
            traceback.print_exc()
            return Response({"problem"}, status=status.HTTP_404_NOT_FOUND)


