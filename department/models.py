from django.db import models

from employee.models import Teacher

class Department(models.Model):
    """
    Model representing a course(e.g. economic sciences).
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=32)
    # school = models.ForeignKey(School, on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=32, decimal_places=2)

    def __str__(self):
        return (self.name)

class Room(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    places = models.IntegerField()

    def __str__(self):
        return (self.name)



class ClassLevel(models.Model):
    """Define objects like first-year, second-year"""
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)


class Subject(models.Model):
    """
    Model representing a course(e.g. Programming, Accounting).
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=32)
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return (self.name)