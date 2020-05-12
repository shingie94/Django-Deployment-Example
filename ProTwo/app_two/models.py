from django.db import models
from django.db.models import Model
from django import forms

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,unique=True)
    last_name = models.CharField(max_length=264,unique=True)
    email = models.EmailField(max_length=256,unique=True)

class My_Model(models.Model):
    first_name = forms.CharField(max_length= 128,required=True)
    last_name = forms.CharField(max_length= 128,required=True)
    email = forms.EmailField(max_length= 128)
