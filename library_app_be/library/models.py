from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=101, blank=True, default='')
    description = models.CharField(max_length=254, blank=True, default='')
    cover_url = models.CharField(max_length=254, blank=True, default='')