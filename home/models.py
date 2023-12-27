# from django.db import models
from django.contrib.gis.db import models


class Natoshi(models.Model):
    nid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    gutno = models.IntegerField()
    crop = models.CharField(max_length=100)
    area = models.FloatField()
    village = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'Natoshi'
