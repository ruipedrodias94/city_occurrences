from django.db import models
from geopy import distance

# Create your models here.


class Occurrence(models.Model):
    description = models.TextField(max_length=200, null=True, blank=True)
    lat = models.FloatField(blank=True, default='')
    lon = models.FloatField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, null=True)
    status = models.TextField(max_length=20, null=True,
                              blank=True, default="POR_VALIDAR")
    category = models.TextField(max_length=20, null=True, blank=True)
    distance_from_hq = models.FloatField(blank=True, default='')
    author = models.ForeignKey(
        'auth.User', related_name='occurrences', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at', 'status']

    def get_distance_from_hq(self, lat, lon):
        coords_1 = (40.646860, -8.642999)
        coords_2 = (lat, lon)
        return distance.distance(coords_1, coords_2).km

    def __str__(self):
        '''
        String representation of the occurrence
        '''
        return 'Description: {}, created_at: {}, status: {}, category:{}'.format(self.description, self.created_at, self.status, self.category)

    def save(self, *args, **kwargs):
        self.distance_from_hq = self.get_distance_from_hq(self.lat, self.lon)
        super().save(*args, **kwargs)
