# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import *

@csrf_exempt
def send_table_data(request,name):

    if request.method=='GET':
        if name=='households':
            household = households.objects.all()
            serializer = households_serializer(household, many=True)
            return JsonResponse(serializer.data, safe=False)
        if name=='person':
            persons = person.objects.all()
            serializer = person_serializer(persons, many=True)
            return JsonResponse(serializer.data, safe=False)
        if name=='farm':
            farms = farm.objects.all()
            serializer = farm_serializer(farms, many=True)
            return JsonResponse(serializer.data, safe=False)
        if name=='farmshape':
            shapes = farm_shape.objects.all()
            serializer = farm_shape_serializer(shapes, many=True)
            return JsonResponse(serializer.data, safe=False)
        if name=='crops':
            crop = crops.objects.all()
            serializer = crops_serializer(crop, many=True)
            return JsonResponse(serializer.data, safe=False)
        if name=='seasonwisecrop':
            season = season_wise_crop.objects.all()
            serializer = season_wise_crop_serializer(season, many=True)
            return JsonResponse(serializer.data, safe=False)
        if name=='wells':
            well = wells.objects.all()
            serializer = wells_serializer(well, many=True)
            return JsonResponse(serializer.data, safe=False)
        if name=='wellobservations':
            observations = well_observations.objects.all()
            serializer = well_observations_serializer(observations, many=True)
            return JsonResponse(serializer.data, safe=False)


from django.shortcuts import render

# Create your views here.
