from django.db import models

from department.models import Department

class School(models.Model):
    """
    Model representing a school (e.g. University of cambridge).
    """
    name = models.CharField(max_length=100)
    abreviation = models.CharField(max_length=16)
    logo = models.ImageField(null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    adress_1 = models.CharField(max_length=200)
    adress_2 = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=32)
    fax = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    authorization_number = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return (self.name)


class Batch(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return (self.name)