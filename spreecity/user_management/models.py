from django.db import models


# Create your models here.
class Member(models.Model):
    first_name             = models.CharField(max_length = 150)
    last_name              = models.CharField(max_length = 150)
    country                = models.CharField(max_length = 150)
    city                   = models.CharField(max_length = 150)
    email                  = models.EmailField(max_length = 30)
    gender                 = models.CharField(max_length = 150)
    date                   = models.DateField()
    
# Create your models here.
class Partner(models.Model):
    company_name             = models.CharField(max_length = 150)
    company_country          = models.CharField(max_length = 150)
    business_name            = models.CharField(max_length = 150)
    business_type            = models.CharField(max_length = 150)
    business_description     = models.TextField()
    mailling_address         = models.TextField()
    zipcode                  = models.CharField(max_length = 15)
    country                  = models.CharField(max_length = 150)
    state                    = models.CharField(max_length = 150, blank = True, null = True)
    city                     = models.CharField(max_length = 150, blank = True, null = True)
    update                   = models.BooleanField(default = True)