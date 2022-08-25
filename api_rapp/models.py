from django.db import models

# Create your models here.


class Phones(models.Model):
    phone = models.CharField(max_length=12, blank=True, null=True)
    entity_id = models.CharField(max_length=255, blank=True, null=True)
    snils = models.CharField(max_length=20, blank=True, null=True)
    oiv_id = models.IntegerField(blank=True, null=True)
    theme_id = models.BigIntegerField(blank=True, null=True)
    request_id = models.IntegerField(blank=True, null=True)
    id_dt = models.DateTimeField(blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    call_duration_category = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.phone}"



