from django.db import models
from django.urls import reverse

class Joshi(models.Model):
    name = models.CharField(max_length=100)
    promotion = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age = models.IntegerField()
    finisher = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'joshi_id': self.id})
