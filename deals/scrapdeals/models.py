from django.db import models
from django import forms

class SubscribeForm(forms.Form):
    email = forms.EmailField()

class SubscribeModel(models.Model):
    email = models.EmailField(unique=True)
