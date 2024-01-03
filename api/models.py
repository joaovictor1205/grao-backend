from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class Food(models.Model): 
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, default=None)
    price = models.DecimalField(max_length=100, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, default=None)
    price = models.DecimalField(max_length=100, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100, default=None, null=True)
    drink = models.ManyToManyField(Drink)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return self.name

class AppUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

class AppUser(AbstractBaseUser, PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'

    objects = AppUserManager()
    def __str__(self):
	    return self.username
