from rest_framework import serializers

from .models import *

class households_serializer(serializers.ModelSerializer):
    class Meta:
        model=households
        fields=('id','latitude','longitude','monthly_income','person_count','house_image','image_link')

    def create(self, validated_data):

        return households.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.monthly_income = validated_data.get('monthly_income', instance.monthly_income)
        instance.person_count = validated_data.get('person_count', instance.person_count)
        instance.house_image = validated_data.get('house_image', instance.house_image)
        instance.image_link = validated_data.get('image_link', instance.image_link)
        instance.save()
        return instance

class person_serializer(serializers.ModelSerializer):
    class Meta:
        model=person
        fields=('id','house_id','person_name','gender','date_of_birth')

    def create(self, validated_data):

        return person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.house_id = validated_data.get('house_id', instance.house_id)
        instance.person_name = validated_data.get('person_name', instance.person_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth=validated_data.get('date_of_birth',instance.date_of_birth)
        instance.save()
        return instance

class farm_serializer(serializers.ModelSerializer):
    class Meta:
        model=farm
        fields=('id','house_id','farm_area','farm_points','farm_link')

    def create(self, validated_data):

        return farm.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.house_id = validated_data.get('house_id', instance.house_id)
        instance.farm_area = validated_data.get('farm_area', instance.farm_area)
        instance.farm_points = validated_data.get('farm_points', instance.farm_points)
        instance.farm_link = validated_data.get('farm_link', instance.farm_link)
        instance.save()
        return instance

class farm_shape_serializer(serializers.ModelSerializer):
    class Meta:
        model=farm_shape
        fields=('farm_id','lat','lon','sequence_number')

    def create(self, validated_data):

        return farm_shape.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.sequence_number = validated_data.get('sequence_number', instance.sequence_number)
        instance.save()
        return instance

class crops_serializer(serializers.ModelSerializer):
    class Meta:
        model=crops
        fields=('id','crop_name')

    def create(self, validated_data):

        return crops.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.crop_name = validated_data.get('crop_name', instance.crop_name)
        instance.save()
        return instance

class season_wise_crop_serializer(serializers.ModelSerializer):
    class Meta:
        model=season_wise_crop
        fields=('id','season_name','crop_name','farm_id','area_cultivated')

    def create(self, validated_data):

        return season_wise_crop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.season_name = validated_data.get('season_name', instance.season_name)
        instance.crop_name = validated_data.get('crop_name', instance.crop_name)
        instance.farm_id = validated_data.get('farm_id', instance.farm_id)
        instance.area_cultivated=validated_data.get('area_cultivated',instance.area_cultivated)
        instance.save()
        return instance

class wells_serializer(serializers.ModelSerializer):
    class Meta:
        model=wells
        fields=('id','latitude','longitude','depth','avg_water_yield')

    def create(self, validated_data):

        return wells.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.depth = validated_data.get('depth', instance.depth)
        instance.avg_water_yield = validated_data.get('avg_water_yield', instance.avg_water_yield)
        instance.save()
        return instance

class well_observations_serializer(serializers.ModelSerializer):
    class Meta:
        model=well_observations
        fields=('id','date_time','well_id','water_yield')

    def create(self, validated_data):

        return well_observations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.well_id = validated_data.get('well_id', instance.well_id)
        instance.water_yield = validated_data.get('water_yield', instance.water_yield)
        instance.save()
        return instance