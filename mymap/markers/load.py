import os
from django.contrib.gis.utils import LayerMapping
from .models import Neighborhood

# Auto-generated `LayerMapping` dictionary for Neighborhood model
neighborhood_mapping = {
    'geom': 'MULTIPOLYGON',
}


neighborhood_shapefile = '/home/augusto/Projects/geodjango/mymap/geo_export_260ff6e1-c4bf-45d2-b17d-45d9e8fb6dc2.shp'

def run(verbose=True):
    layermap = LayerMapping(Neighborhood,neighborhood_shapefile,neighborhood_mapping,transform=False)
    layermap.save(strict=True,verbose=verbose)