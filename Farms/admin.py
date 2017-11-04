# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from .models import *
admin.site.register(households)
admin.site.register(farm,admin.OSMGeoAdmin)
admin.site.register(farm_shape)
admin.site.register(person)
admin.site.register(crops)
admin.site.register(season_wise_crop)
admin.site.register(well_observations)
admin.site.register(wells)

