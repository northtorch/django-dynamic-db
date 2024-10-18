from django.db import models


class MasterCountData(models.Model):
    count = models.IntegerField(
        'マスターカウンタ',
        default=0,
        null=False,
        blank=False,
    )
