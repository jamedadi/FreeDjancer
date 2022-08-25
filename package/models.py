from django.db import models

from utils.basemodel import BaseModel


class Package(BaseModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    bids = models.PositiveSmallIntegerField()
    price = models.PositiveBigIntegerField()

    class Meta:
        verbose_name = 'package'
        verbose_name_plural = 'packages'

    def __str__(self):
        return self.title
