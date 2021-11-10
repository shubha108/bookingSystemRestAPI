from django.db import models

# Create your models here.

# user model with userid , username , Email , password
class User(models.Model):
    userid = models.AutoField(primary_key=True , unique=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50 , unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    


# advisor model with advisorid , advisor_name, advisor_img
class Advisor(models.Model):
    advisorid = models.AutoField(primary_key=True , unique=True)
    advisor_name = models.CharField(max_length=50 ,)
    advisor_img = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
# booking calls with userid and advisor name , advisor id ,advisor photo, date , time in mongodb with userid , advisor id , advisor name , advisor photo , date , time
class Booking(models.Model):
    userid = models.IntegerField()
    advisorid = models.IntegerField()
    advisor_name = models.CharField(max_length=50)
    advisor_img = models.CharField(max_length=50)
    booking_date = models.DateField(max_length=50)
    booking_time = models.TimeField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    
