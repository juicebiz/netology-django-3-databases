from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)
