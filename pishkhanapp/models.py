from django.db import models
from django.contrib.auth.models import User

CHOICES = [
    ('DrivingLiscense', 'DrivingLiscense'),
    ('Passport', 'Passport'),
    ('SSCard', 'SSCard'),
    ('Violation', 'Violation'),
]
length = 25
# Create your models here.
class userfile(models.Model):
    firstname = models.CharField(max_length=length, blank=True, null=True)
    lastname = models.CharField(max_length=length, blank=True, null=True)
    ssn = models.IntegerField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    birthlocation = models.CharField(max_length=length, blank=True, null=True)
    user = models.OneToOneField(User , on_delete = models.CASCADE)

    def __str__(self):
        return self.firstname


class medicalForm(models.Model):
    firstname = models.CharField(max_length=length, blank=True, null=True)
    lastname = models.CharField(max_length=length, blank=True, null=True)
    ssn = models.IntegerField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    result = models.FileField( upload_to=None, max_length=100)

    

    class Meta:
        verbose_name = ("medicalform")
        verbose_name_plural = ("medicalforms")

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse("medicalform_detail", kwargs={"pk": self.pk})

class violation(models.Model):
    name = models.CharField(max_length=length, blank=True, null=True, choices=CHOICES,)
    policenum = models.IntegerField()
    carnum = models.IntegerField()
    filenum = models.ForeignKey("pishkhanapp.userfile",  on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("violation")
        verbose_name_plural = ("violations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("violation_detail", kwargs={"pk": self.pk})

class service(models.Model):
    typeofservice  = models.CharField(max_length=length, blank=True, null=True)
    servicedate = models.DateField(auto_now=False, auto_now_add=False)    
    filenum = models.ForeignKey("pishkhanapp.userfile",  on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("service")
        verbose_name_plural = ("services")

    def __str__(self):
        return self.typeofservice

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"pk": self.pk})


class resultreq(models.Model):
    filenum = models.ForeignKey("pishkhanapp.userfile", on_delete=models.CASCADE)
    regnum = models.IntegerField()
    result = models.FileField( upload_to=None, max_length=100)
    

    class Meta:
        verbose_name = ("resultreq")
        verbose_name_plural = ("resultreqs")

    def get_absolute_url(self):
        return reverse("resultreq_detail", kwargs={"pk": self.pk})
