from django.contrib import admin
from .models import Restaurant, Drink, Food

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Drink)
admin.site.register(Food)
