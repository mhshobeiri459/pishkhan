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
    ssn = models.IntegerField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    birthlocation = models.CharField(max_length=length, blank=True, null=True)
    user = models.OneToOneField(User , on_delete = models.CASCADE)



class medicalForm(models.Model):
    result = models.ImageField( upload_to='media', max_length=100,blank = True, default="default.png")
    filenum = models.ForeignKey("pishkhanapp.userfile",  on_delete=models.CASCADE)


    

    class Meta:
        verbose_name = ("medicalform")
        verbose_name_plural = ("medicalforms")

    def __str__(self):
        return self.filenum

    def get_absolute_url(self):
        return reverse("medicalform_detail", kwargs={"pk": self.pk})

class violation(models.Model):
    policenum = models.IntegerField()
    carnum = models.IntegerField()
    motornum = models.IntegerField()
    cartype = models.CharField(max_length=30,null=True)
    filenum = models.ForeignKey("pishkhanapp.userfile", on_delete=models.CASCADE) 

    class Meta:
        verbose_name = ("violation")
        verbose_name_plural = ("violations")


    def get_absolute_url(self):
        return reverse("violation_detail", kwargs={"pk": self.pk})

class service(models.Model):
    typeofservice  = models.CharField(max_length=length, blank=True, null=True, choices=CHOICES)
    servicedate = models.DateField(auto_now=False, auto_now_add=False) 
    filenum = models.ForeignKey("pishkhanapp.userfile", on_delete=models.CASCADE)   
    result = models.OneToOneField("pishkhanapp.resultreq",  on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = ("service")
        verbose_name_plural = ("services")

    def __str__(self):
        return self.typeofservice

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"pk": self.pk})


class resultreq(models.Model):
    result = models.ImageField( upload_to='media', max_length=100,blank = True, default="default.png")
    

    class Meta:
        verbose_name = ("resultreq")
        verbose_name_plural = ("resultreqs")

    def get_absolute_url(self):
        return reverse("resultreq_detail", kwargs={"pk": self.pk})

class files_archive(models.Model):
    filenum = models.ForeignKey("pishkhanapp.userfile",  on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey("pishkhanapp.service",   on_delete=models.CASCADE, null=True, blank=True)
    perimage = models.ImageField(upload_to='media')
    militimage = models.ImageField(upload_to='media')
    medimage = models.ImageField(upload_to='media')
    natimage = models.ImageField(upload_to='media')
    

class deliveries(models.Model): 
    address = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("deliveries")
        verbose_name_plural = ("deliveriess")

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse("deliveries_detail", kwargs={"pk": self.pk})
