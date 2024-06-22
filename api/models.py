from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    # Interests
    walk = models.BooleanField(default=False, null=True)
    coffee = models.BooleanField(default=False, null=True)
    tea = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"{self.name}, {self.city}"
