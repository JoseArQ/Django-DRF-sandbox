from django.db import models

class Level(models.Model):
    level = models.CharField(max_length=40)
    score = models.IntegerField()

class Question(models.Model):
    question = models.CharField(max_length=200)
    level = models.OneToOneField(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.question