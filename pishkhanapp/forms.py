from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)

CHOICES=[('1','27 بهمن 1399'),
         ('2','28 بهمن 1399'),
         ('3','29 بهمن 1399'),
         ('4','30 بهمن 1399')]

class DriveForm(forms.ModelForm):
    
    class Meta:
        model = files_archive
        fields = ['perimage', 'militimage', 'medimage']
        labels = {
            "perimage": 'عکس پرسنلی (4*3)',
            'militimage' : 'عکس پایان خدمت یا معافیت تحصیلی',
            'medimage' : 'مدرک پزشکی',
        }

class NationalForm(forms.ModelForm):
    
    class Meta:
        model = files_archive
        fields = ['perimage',  'medimage']
        labels = {
            "perimage": 'عکس پرسنلی (4*3)',
            'medimage' : 'مدرک پزشکی',
        }

class PassForm(forms.ModelForm):
    class Meta:
        model = files_archive
        fields = ['perimage', 'militimage', 'natimage']
        labels = {
            "perimage": 'عکس پرسنلی (4*3)',
            'militimage' : 'عکس پایان خدمت یا معافیت تحصیلی',
            'natimage' : ' کارت ملی '
        }
        
class FollowupForm(forms.Form):
    followupcode = forms.IntegerField(required=True, label='کد پیگیری')


class violationForm(forms.Form):
    ownername = forms.CharField(max_length=20,required=True, label='نام مالک خودرو')
    carnum = forms.IntegerField(required=True, label='شماره پلاک')
    motornum = forms.IntegerField(required=True, label='شماره موتور')
    cartype = forms.CharField(max_length=20, required=True, label='نوع ماشین')
    policenum = forms.CharField(max_length=20, required=True, label='شماره انتظامی')

class SignUpForm(UserCreationForm):
    firstname = forms.CharField( max_length=20, required=False, label='نام')
    lastname = forms.CharField( max_length=20, required=False, label='نام خانوادگی')
    email = forms.CharField( max_length=50, required=True, label='ایمیل')
    ssn = forms.IntegerField(label='کد ملی')
    birthdate = forms.DateField(label='تاریخ تولد',widget=forms.DateInput(attrs={'type': 'date'}))
    birthlocation = forms.CharFieldlabel=('محل تولد')
    password1 = forms.CharField(
        label="رمز عبور",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=None
    )
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="برای تایید رمز عبور قبلی را دوباره وارد نمایید",
    )


    
class DeliveryForm(forms.Form):
    address = forms.CharField(max_length=50, label='آدرس')
    date = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect, label='تاریخ')
    

    
