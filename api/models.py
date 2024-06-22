from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    # Interests
    walk = models.BooleanField(default=False)
    coffee = models.BooleanField(default=False)
    tea = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}, {self.city}"
