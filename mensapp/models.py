from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
CATEGORY_CHOICES = (
    ('casual', 'CASUAL'),
    ('formal', 'FORMAL'),
    ('semi-formal', 'SEMI-FORMAL'))

MAIN_CATEGORY = (
    ('mens', 'MENS'),
    ('ladies', 'LADIES'),
    ('girls', 'GIRLS'),
    ('boys', 'BOYS'),
    ('kids', 'KIDS'))

DESIGNBY = (
    ('Anas NS', 'ANAS'),
    ('Sajith VP', 'SAJITH'),
    ('Diljith K', 'DILJITH'))

class tmens(models.Model):
    def __str__(self):
        return self.name

    img = models.ImageField(upload_to='picture')
    name = models.CharField(max_length=100)
    maincategory = models.CharField(max_length=20, choices=MAIN_CATEGORY, default='mens')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='casual')
    rating = models.FloatField(default=0)
    cartflag= models.BooleanField(default=False)
    designedby = models.CharField(max_length=20, choices=DESIGNBY, default='Anas NS')


class ratingreview(models.Model):
    product = models.ForeignKey(tmens, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(max_length=500, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # @classmethod
    # def set_rating(cls,rating):
    #     rating=cls(rating=rating)
    #     return rating
