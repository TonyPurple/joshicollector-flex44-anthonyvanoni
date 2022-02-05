from django.db import models
from django.urls import reverse
from datetime import date

BOOKINGS = (
  ('D', 'Dojo Training'),
  ('S', 'Singles Match'),
  ('T', 'Tag Match'),
  ('U', 'Unit Match'),
  ('G', 'Gimmick Match'),
  ('M', 'Media Appearance')
)

class Item(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('items_detail', kwargs={'pk': self.id})

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
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'joshi_id': self.id})

    def overall(self):
      overall = ((self.itfactor + self.technique + self.power + self.speed + self.striking + self.aerial) /6)
      overall_round = round(overall, 1)
      return overall_round
    
    def booked_for_today(self):
      return self.booking_set.filter(date=date.today()).count() >= 3

class Booking(models.Model):
  date = models.DateField('booking date')
  booking = models.CharField(
    max_length=1,
    choices=BOOKINGS,
    default=BOOKINGS[0][0]
  )
  joshi = models.ForeignKey(Joshi, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_booking_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']
