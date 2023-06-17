from django.db import models

# Create your models here.
class ResourceModel(models.Model):
    name = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)
