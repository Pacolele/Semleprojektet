from django.db import models

# Create your models here.


class Semlor(models.Model):
    def __str__(self):
        return self.bakery
    bakery = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    picture_name = models.CharField(max_length=200)
    vegan = models.BooleanField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    kind = models.CharField(max_length=50)


class Rating(models.Model):
    def __str__(self):
        return str(self.rating)
    semla = models.ForeignKey(
        Semlor, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(default=0)
