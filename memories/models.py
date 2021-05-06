from django.db import models


class MemoryModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    user_id = models.IntegerField(blank=False, null=False)
    location_name = models.CharField(max_length=150, blank=False, null=False)
    location_address = models.CharField(max_length=255, blank=False, null=False)
    location_memories = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'memories'
        verbose_name = 'Memory'
        verbose_name_plural = 'Memories'
