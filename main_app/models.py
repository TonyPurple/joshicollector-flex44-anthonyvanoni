from django.db import models
from django.urls import reverse

class Joshi(models.Model):
    name = models.CharField(max_length=100)
    promotion = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    finisher = models.CharField(max_length=100)
    age = models.IntegerField()
    itfactor = models.IntegerField(default=50)
    technique = models.IntegerField(default=50)
    power= models.IntegerField(default=50)
    speed = models.IntegerField(default=50)
    striking = models.IntegerField(default=50)
    aerial = models.IntegerField(default=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'joshi_id': self.id})

