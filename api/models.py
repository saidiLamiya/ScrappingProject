from django.db import models
from django.contrib import admin

# Create your models here.


class User(models.Model):
    #list_display= ('first_name', 'last_name', 'school', 'email')
    # id = models.CharField(max_length=8, default="", unique=True)
    email = models.CharField("email",max_length=100, unique=True)
    first_name = models.CharField("first name",max_length=50, default="")
    last_name = models.CharField("last name",max_length=50, default="")
    school = models.CharField("school",max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    city_of_origin = models.CharField(max_length=50, default="")
    current_city = models.CharField(max_length=50, default="")
    joined_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.school} {self.email} "

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='frontend/static/images',max_length=1000)
    button = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title} {self.description}"

class School(models.Model):
    name = models.CharField(max_length=50, default="")
    def __str__(self):
        return f"{self.name}"

class Keyword(models.Model):
    keyword = models.CharField(max_length=50, default="")
    def __str__(self):
        return f"{self.keyword}"



