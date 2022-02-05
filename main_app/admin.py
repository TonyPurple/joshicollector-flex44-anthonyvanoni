from django.contrib import admin
# import your models here
from .models import Joshi, Item

# Register your models here
admin.site.register(Joshi)
admin.site.register(Item)
