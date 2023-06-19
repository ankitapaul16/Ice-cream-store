from django.db import models

# Create your models here.
class Contact(models.Model):
    serial_number = models.CharField(max_length=3)
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    country_name= models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    city =models.CharField(max_length=20)
    state =models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    address_1= models.CharField(max_length=1000)
    address_2=models.CharField(max_length=1000)
    email_address=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    comments = models.TextField()
    date=models.DateField()
   
   
def __str__(self):
       return self.name
   