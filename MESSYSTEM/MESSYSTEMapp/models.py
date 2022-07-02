from random import choices
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser


from django.forms import CharField


class registration(AbstractUser):
    _adviser = [
        ('Admin','Admin'),
        ('Adviser','Adviser'),
        ('Pambid','Ms. Gina Pambid'),
        ('Pendo','Mrs. Aurea Pendo'),
        ('Loresca','Ms. Adelia Loresca'),
        ('Bocar','Mrs. Maria Lina Bocar'),
        ('Camcho','Ms. Ella Mae Camcho'),
        ('Neypes','Mr. Khristine Neypes'),
        ('Niemes','Renee Rose Niemes'),
        ('Apostol','Mrs. Teresita Apostol')
    ] 

    _gradelvl = [
        ('Admin','Admin'),
        ('Adviser','Adviser'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6')
    ]

    _section = [
        ('Admin','Admin'),
        ('Adviser','Adviser'),
        ('A','Section A'),
        ('B','Section B'),
        ('C','Section C'),
        ('D','Section D'),
        ('E','Section E'),
        ('F','Section F'),
        ('G','Section G'),
    ]

    _userType = [
        ('Adviser','Adviser'),
        ('Student','Student'),
        ('Admin','Admin')
    ]

    contacts = models.CharField(max_length=11, unique=True, verbose_name='contacts')
    parents = models.CharField(max_length=100, verbose_name='parents')
    adviser = models.CharField(max_length=50, choices = _adviser, verbose_name='adviser')
    gradelvl = models.CharField(max_length=11,choices = _gradelvl, verbose_name='gradelvl')
    section = models.CharField(max_length=50,choices= _section, verbose_name='section')
    lrn = models.CharField(max_length=20, unique=True, primary_key=True)
    userType = models.CharField(max_length=50, choices= _userType, verbose_name='userType')


class make_announcement(models.Model):
    ret = models.DateField(verbose_name='retrieval')
    subm = models.DateField(verbose_name='submission')

class studentInfo(models.Model):
    lrn_student = models.OneToOneField(registration, on_delete=models.CASCADE, primary_key=True,verbose_name='student_id')
    username = models.CharField(max_length=20, blank=False,verbose_name='name')
    quarter = models.CharField(max_length=20,verbose_name='quarter')
    week = models.CharField(max_length=20,verbose_name='week')
    modules = models.CharField(max_length=20,verbose_name='modules')
    status = models.CharField(max_length=20,verbose_name='status')

class scholarship(models.Model):
    _amount = [
        ('1000','1000'),
        ('2000','2000'),
        ('3000','3000')
    ]

    lrn_scholarship = models.OneToOneField(studentInfo, on_delete=models.CASCADE, primary_key=True,verbose_name='scholarship_id')
    username = models.CharField(max_length=20, blank=False,verbose_name='name')
    amount = models.CharField(max_length=50, choices= _amount, verbose_name='amount')







