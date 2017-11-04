from django.db import models
from django_countries.fields import CountryField



class Employee(models.Model):
    SELECT_GENDER = (
        ('male', 'Male'), ('female', 'Female'),(None, 'Select gender')
        )

    employee_number = models.CharField(max_length=64)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    genre = models.CharField(max_length=32, choices=SELECT_GENDER)
    nationality = CountryField(blank_label='(select country)')
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=32)
    email = models.CharField(max_length=100, null=True, blank=True)
    id_card_number = models.CharField(max_length=64)
    job_type = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    ssn = models.CharField(max_length=64)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Teacher(Employee):
    
    title = models.CharField(max_length=100) 

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)