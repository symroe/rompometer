from django.db import models
import datetime


class Romp(models.Model):
    title = models.CharField(blank=True, max_length=255)
    link = models.URLField(blank=True, verify_exists=True)
    date = models.DateField(default=datetime.datetime.today)
    paper = models.CharField(blank=True, max_length=100)