# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class households(models.Model):
    #house_id=models.IntegerField(primary_key='true')
    latitude=models.DecimalField(max_digits=10, decimal_places=6)
    longitude=models.DecimalField(max_digits=10, decimal_places=6)
    monthly_income=models.IntegerField()
    person_count=models.IntegerField(default=1)
    house_image=models.ImageField()
    image_link=models.CharField(max_length=1000)

    def __str__(self):
        return '%s' %(self.id)

class person(models.Model):
    #person_id=models.IntegerField(primary_key='true')
    house_id=models.ForeignKey(households,on_delete=models.CASCADE)
    person_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=1)
    date_of_birth=models.DateField()

    def __str__(self):
        return self.person_name

class farm(models.Model):
    #farm_id=models.IntegerField(primary_key='true')
    house_id = models.ForeignKey(households, on_delete=models.CASCADE)
    farm_area = models.FloatField()
    farm_points=models.PolygonField(default='POLYGON(( 10 10, 10 20, 20 20, 20 15, 10 10))')
    farm_link=models.CharField(max_length=1000,default='https://image.ibb.co/c13FGG/farm.jpg')

    def __str__(self):
        return '%s'%(self.id)

class farm_shape(models.Model):
    farm_id=models.ForeignKey(farm,on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lon = models.DecimalField(max_digits=10, decimal_places=6)
    sequence_number = models.IntegerField()

    def __str__(self):
        return '%s'%( self.farm_id)

class crops(models.Model):
    #crop_id=models.IntegerField(primary_key='true')
    crop_name=models.CharField(max_length=30)

    def __str__(self):
        return self.crop_name

class season_wise_crop(models.Model):
    season_name=models.CharField(max_length=20)
    #crop_id=models.ForeignKey(crops,on_delete=models.CASCADE)
    crop_name=models.CharField(default="Rice",max_length=20)
    farm_id=models.ForeignKey(farm,on_delete=models.CASCADE)
    area_cultivated=models.FloatField()

    def __str__(self):
        return '%s'%(self.farm_id)

class wells(models.Model):
    #well_id=models.IntegerField(primary_key='true')
    farm_id=models.ForeignKey(farm,on_delete=models.CASCADE)
    latitude=models.DecimalField(max_digits=10,decimal_places=6)
    longitude=models.DecimalField(max_digits=10,decimal_places=6)
    depth=models.FloatField()
    avg_water_yield=models.FloatField()

    def __str__(self):
        return '%s'%(self.id)

class well_observations(models.Model):
    date_time=models.DateTimeField()
    well_id=models.ForeignKey(wells,on_delete=models.CASCADE)
    water_yield=models.FloatField()

    def __str__(self):
        return '%s'%(self.well_id)

