from django.db import models

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=255)
    slug = models.SlugField(max_length=15)


