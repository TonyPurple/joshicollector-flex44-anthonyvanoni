from django.contrib import admin
# import your models here
from .models import Joshi, Item, Booking, Photo

# Register your models here
admin.site.register(Joshi)
admin.site.register(Item)
admin.site.register(Booking)
admin.site.register(Photo)
