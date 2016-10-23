from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Temperature(models.Model):
    temperature_id = models.AutoField(primary_key=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temperature'
