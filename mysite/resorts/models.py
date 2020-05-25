from django.db import models

# Create your models here.

class ResortName(models.Model):
    Resort_name_text = models.CharField(max_length=500)
    booking_date = models.DateTimeField('date booked')

    def __str__(self):
        return self.Resort_name_text

class Dish(models.Model):
    Dish_name_text = models.CharField(max_length=300)
    resortD = models.ForeignKey(ResortName, on_delete=models.CASCADE)

    def __str__(self):
        return self.Dish_name_text

class ResortReview(models.Model):
    Resort_review_text = models.CharField(max_length=600)
    resortR = models.ForeignKey(ResortName, on_delete=models.CASCADE)

    def __str__(self):
        return self.Resort_review_text
