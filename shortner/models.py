from django.db import models


class ShortUrl(models.Model):
    url_id = models.CharField(max_length=30)
    full_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
