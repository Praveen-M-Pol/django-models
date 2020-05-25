from django.contrib import admin

# Register your models here.

from .models import ResortName, Dish, ResortReview

admin.site.register(ResortName)
admin.site.register(Dish)
admin.site.register(ResortReview)