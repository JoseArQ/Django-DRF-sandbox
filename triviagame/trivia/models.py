from django.db import models

class Level(models.Model):
    level = models.CharField(max_length=40)
    score = models.IntegerField()