from django.db import models


class Semlor(models.Model):
    def __str__(self):
        return self.bakery

    @property
    def avg_rating(self):
        return getattr(self, '_annotated_avg', None) or self.ratings.aggregate(
            models.Avg('rating'))['rating__avg']
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
    comment = models.CharField(max_length=400, blank=True)
