from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['walk', 'coffee', 'tea']
