from django.db import models
from django_countries.fields import CountryField
from school.models import Batch, School
from department.models import Department, ClassLevel

import datetime

# Create your models here.
SELECT_GENDER = (
        ('male', 'Male'), ('female', 'Female'),(None, 'Select Gender')
        )

def registration_number():
    current_year = datetime.date.today().year
    last_reg = Registration.objects.latest('id')
    if not last_reg:
        return("Reg-%d-%08d" % (current_year, 1))
    last_id = last_reg.id
    current_id = int(last_id) + 1
    return ("Reg-%d-%08d" % (current_year, current_id))


class Registration(models.Model):
    """
    Model representing a person(e.g. mohamed jalloh).
    """
    registration_number = models.CharField(max_length=20, default=registration_number, unique=True, editable=False)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    genre = models.CharField(max_length=32, choices=SELECT_GENDER)
    nationality = CountryField(blank_label='(select country)')
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=32)
    email = models.CharField(max_length=100, null=True, blank=True)
    id_card_number = models.CharField(max_length=64)
    guardian = models.CharField(max_length=100)
    guardian_adress = models.CharField(max_length=200)
    guardian_phone = models.CharField(max_length=32)
    guardian_email = models.CharField(max_length=100, null=True, blank=True)
    school_origin = models.CharField(max_length=100)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


def student_number():
    school = School.objects.get(pk=1)
    if not school:
        raise("there should be a school")
    school_abbr = school.abreviation
    school_str = school_abbr[:2]
    current_year = datetime.date.today().year
    last_student = Admission.objects.latest('id')
    if not last_student:
        return("%s-%d-%08d" % (school_str, current_year, 1))
    last_id = last_student.id
    current_id = int(last_id) + 1
    return("%s-%d-%08d" % (school_str, current_year, 1))


class Admission(models.Model):
    student_card_number = models.CharField(max_length=20, default= student_number, unique=True, editable=False)
    date = models.DateField()
    batch = models.ForeignKey(Batch)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    registree = models.OneToOneField(Registration)
    class_level =models.ForeignKey(ClassLevel, on_delete=models.CASCADE)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return (self.registree.first_name)