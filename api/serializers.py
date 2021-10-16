from django.db.models import fields
from rest_framework import serializers
from .models import User, Event, School, Keyword


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'school',
                  'city_of_origin', 'current_city', 'email', 'joined_at')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields that we wanna set as part of the post request
        fields = ('first_name', 'last_name', 'phone', 'school',
                  'city_of_origin', 'current_city', 'email')

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(validators = [])

    class Meta:
        model = User
        # fields that we wanna set as part of the post request
        fields = ('first_name', 'last_name', 'phone', 'school',
                  'city_of_origin', 'current_city', 'email')                  


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'photo', 'button')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school')

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'keyword')

