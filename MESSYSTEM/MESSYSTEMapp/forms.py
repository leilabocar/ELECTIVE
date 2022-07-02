from dataclasses import field
import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.mail import send_mail



class loginForm (forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Username: ',
                "class": "form-control"
            }                                                               
        )
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "placeholder": 'Password: ',
                "class": "form-control"
            }
        )
    )

class searchForm (forms.Form):
    search = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Search: ',
                "class": "form-control-sm float-md-right"
            }                                                               
        )
    )
    
class StudentSignupForm(UserCreationForm):
    _userType = [
        ('Adviser','Adviser'),
        ('Student','Student'),
        ('Admin','Admin')
    ]

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
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6)
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

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Username',
                "class": "form-control"
            }
        )
    )
   
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "placeholder": 'Password',
                "class": "form-control"
            }
        )
    )
    
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "placeholder": 'Confirm Password',
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        widget= forms.EmailInput(
            attrs={
                "placeholder": 'Gmail Only',
                "class": "form-control"
            }

        )
    )

    parents = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Parents',
                "class": "form-control"
            }
        )
    )
    
    adviser = forms.CharField(
        widget = forms.Select(
            choices= _adviser
            ,attrs={
                "placeholder": 'Adviser',
                "class": "form-control"
            }
        )
    )

    gradelvl = forms.CharField(
        widget = forms.Select(
            choices= _gradelvl
            ,attrs={
                "placeholder": 'Grade Level',
                "class": "form-control"
            }
        )
    )

    section = forms.CharField(
        widget = forms.Select(
            choices= _section
            ,attrs={
                "placeholder": 'Section',
                "class": "form-control"
            }
        )
    )

    lrn = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Lrn',
                "class": "form-control"
            }
        )
    )

    contacts = forms.CharField(
        widget = forms.NumberInput(
            attrs={
                "placeholder": 'Ex: 09123456781',
                "class": "form-control",
                "maxlength": 11
            }
        )
    )

    userType = forms.CharField(
        widget = forms.Select(
            choices= _userType
            ,attrs={
                "placeholder": 'Section',
                "class": "form-control"
            }
        )
    )

    class Meta():
        model = registration
        fields = ('username', 'password1', 'password2', 'parents', 'adviser', 'gradelvl', 'section', 'lrn', 'contacts', 'userType','email')
    
class announceForm(forms.ModelForm):
    ret = forms.DateField(
        widget = forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date"
            }
        )
    )

    subm = forms.DateField(
        widget = forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date"
            }
        )
    )

    class Meta:
        model = make_announcement
        fields = ('ret','subm')

class distributionRetrievalForm(forms.ModelForm):
    _week = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7)
    ]

    _quarter = [
        ('FIRST','FIRST'),
        ('SECOND','SECOND'),
        ('THIRD','THIRD'),
        ('FOURTH','FOURTH')
    ]
    
    _module = [
        ('Receive','Receive'),
        ('Return','Return')
    ]
    
    _status = [
        ('Approved','Approved'),
        ('Not Approved','Not Approved')
    ]
    

    lrn_student = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Lrn: ',
                "class": "form-control"
            }
        )
    )
    
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Name: ',
                "class": "form-control"
            }
        )
    )

    quarter = forms.CharField(
        widget = forms.Select(
            choices= _quarter
            ,attrs={
                "placeholder": 'Quarter:',
                "class": "form-control"
            }
        )
    )

    week = forms.CharField(
        widget = forms.Select(
            choices= _week
            ,attrs={
                "placeholder": 'Week:',
                "class": "form-control"
            }
        )
    )

    modules = forms.CharField(
        widget = forms.RadioSelect(
            choices= _module
            ,attrs={
                "class": "form-check-inline"
            }
        )
    )

    status = forms.CharField(
        widget = forms.Select(
            choices= _status,
            attrs={
                "placeholder": 'Status: ',
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = studentInfo
        fields = ('lrn_student','username','quarter','week','modules','status')

    def save(self):
        stud = super(distributionRetrievalForm,self).save(commit=False)

        if str(self.cleaned_data.get('modules')) == 'Receive' and str(self.cleaned_data.get('week')) == '7' and str(self.cleaned_data.get('quarter')) == 'FOURTH':
            stud.status == 'Approved'
            stud.save()
        else:
            stud.status == 'Not Approved'
            stud.save()

        return stud


class scholarshipForm(forms.ModelForm):
    _amount = [
        ('1000','1000'),
        ('2000','2000'),
        ('3000','3000')
    ]

    lrn_scholarship = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Lrn: ',
                "class": "form-control"
            }
        )
    )
    
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": 'Name: ',
                "class": "form-control"
            }
        )
    )

    amount = forms.CharField(
        widget = forms.Select(
            choices= _amount
            ,attrs={
                "placeholder": 'Amount:',
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = scholarship
        fields = ('lrn_scholarship','username','amount')
