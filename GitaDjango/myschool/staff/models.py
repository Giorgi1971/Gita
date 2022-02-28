from statistics import mode
from unicodedata import name
from django.db import models

from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=120)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)


class ClassNumber(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField()


class Pupil(models.Model):
    pupilname = models.CharField(max_length=255)
    classnumber = models.ForeignKey(ClassNumber, on_delete=models.CASCADE)

    



