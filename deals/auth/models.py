from django import forms
from django.db import models
from django.contrib.auth.models import User

class UserForm(forms.Form):
	username = forms.CharField()
	firstname = forms.CharField()
	lastname = forms.CharField()
	phone_no = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	subscribe = forms.BooleanField(required=False)


	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('username exists')
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('email exists')
		return email


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	phone_no = models.CharField(max_length=15)

	def __unicode__(self):
		return self.user.username

class WishList(models.Model):
	user = models.ForeignKey(User)
	wishlist = models.CharField(max_length=500)
	deal_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.user.username

