from django import forms
class baseForm(forms.Form):
    perimage = forms.FileField(required=True)
    milimage = forms.FileField(required=True)
    med = forms.FileField(required=True)

class FollowupForm(forms.Form):
    followupcode = forms.IntegerField(required=True)


class DeliveryForm(forms.Form):
    address = forms.CharField(required=True)
    date = forms.DateField(required=True)


class violationForm(forms.Form):
    ownername = forms.CharField(max_length=20,required=True)
    carnum = forms.IntegerField(required=True)
    motornum = forms.IntegerField(required=True)
    cartype = forms.CharField(max_length=20, required=True)
    
