"""Markers models."""

from django.contrib.gis.db import models


class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        """Return string representation."""
        return self.name
    
    
class Neighborhood(models.Model):
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for Neighborhood model
neighborhood_mapping = {
    'geom': 'MULTIPOLYGON',
}