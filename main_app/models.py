from django.db import models

class Joshi(models.Model):
    name = models.CharField(max_length=100)
    promotion = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age = models.IntegerField()
    finisher = models.CharField(max_length=100)

    def __str__(self):
        return self.name
