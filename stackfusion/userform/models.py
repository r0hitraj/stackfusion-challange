from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class form(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(null=True)
    email=models.EmailField('Email', null=False,blank=False,max_length=100, unique=True)
    phone=PhoneNumberField(null=False)

