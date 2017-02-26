from django.db import models

# Create your models here.


class pubs(models.Model):
    entity_id = models.AutoField(primary_key=True)
    pubname = models.CharField(max_length=45, blank=False)
    region=models.IntegerField(blank=False)
    class Meta:
        managed = False
        db_table = 'pubs'
