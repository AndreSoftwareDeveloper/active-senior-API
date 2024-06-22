from rest_framework import serializers
from .models import User, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "age",
            "city",
            "district",
            "walk",
            "coffee",
            "tea",
        )
