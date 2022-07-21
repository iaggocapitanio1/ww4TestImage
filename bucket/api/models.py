from django.db import models


class Images(models.Model):
    owner = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
