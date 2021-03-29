from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from pishkhanapp.forms import * 
from django.views.generic.edit import FormView
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html", {})


class violationListView(ListView):
    model = violation
    template_name = "Violation.html"


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            ssn = form.cleaned_data.get('ssn')
            birthdate = form.cleaned_data.get('birthdate')
            birthlocation = form.cleaned_data.get('birthlocation')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            userfile.objects.create(user=user,ssn=ssn,birthdate=birthdate,birthlocation=birthlocation)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'Register.html', {'form': form})

@login_required
def DrivingLiscense(request):
   
    # If this is a POST request then process the Form data
    if request.method == 'POST' :
        form = DriveForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a form instance and populate it with data from the request (binding):
            formperimage = form.cleaned_data['perimage']
            formmilitimage = form.cleaned_data['militimage']
            formmedimage = form.cleaned_data['medimage']
            userf = userfile.objects.get(user=request.user)
            serv = service.objects.create(filenum=userf,typeofservice='DrivingLiscense',servicedate=datetime.today())
            filesar = files_archive.objects.create(filenum=userf,service=serv,perimage=formperimage,militimage=formmilitimage,medimage=formmedimage)
            messages.info(request, 'کد پیگیری شما ')
            form.save()
            postcontext = {
            'code' : serv.id
            }

            # redirect to a new URL:
            return render(request,'DrivingLiscense.html',postcontext)

    # If this is a GET (or any other method) create the default form.
    else:
        form = DriveForm()

    context = {
        'form': form,
    }

    return render(request, 'DrivingLiscense.html', context)

@login_required
def DrivingLiscenseFollowup(request):
    form = FollowupForm(request.POST or None)
    # If this is a POST request then process the Form data
    if request.method == 'POST' and form.is_valid():

        # Create a form instance and populate it with data from the request (binding):
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
        code = form.cleaned_data['followupcode']
        fol = service.objects.get(id=code)
        results = fol.result
        if not results:
            return HttpResponse("<p> عملیات مورد نظر شما به پایان نرسیده است! </p>")
        res_img = results.result
        postcontext = {
            'res_img' : res_img,
            'code' : code
        }
        return render(request, 'DrivingLiscenseFollowup.html', postcontext)

    # If this is a GET (or any other method) create the default form.
    else:
        form = FollowupForm()

    context = {
        'form': form,
    }

    return render(request, 'DrivingLiscenseFollowup.html', context)

@login_required
def DrivingLiscenseDelivery(request):

    if request.method == 'POST' :
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            address = form.cleaned_data['address']
            date = form.cleaned_data['date']
            deliv = deliveries.objects.create(address=address,date=date)
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
            return redirect('index')

    # If this is a GET (or any other method) create the default form.
    else:
        form = DeliveryForm()

    context = {
        'form': form,
    }


    return render(request, 'DrivingLiscenseDelivery.html', context)

@login_required
def NationalCard(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST' :
        form = NationalForm(request.POST, request.FILES)
        if form.is_valid():
            formperimage = form.cleaned_data['perimage']
            formmedimage = form.cleaned_data['medimage']
            userf = userfile.objects.filter(user=request.user)[0]
            serv = service.objects.create(filenum=userf,typeofservice='SSCard',servicedate=datetime.today())
            filesar = files_archive.objects.create(filenum=userf,service=serv,perimage=formperimage,medimage=formmedimage)
            messages.info(request, 'کد پیگیری شما ')
            form.save()
            postcontext = {
            'code' : serv.id
            }

            # redirect to a new URL:
            return render(request,'NationalCard.html',postcontext)
    # If this is a GET (or any other method) create the default form.
    else:
        form = NationalForm()

    context = {
        'form': form,
    }

    return render(request, 'NationalCard.html', context)

@login_required
def NationalCardFollowup(request):

    form = FollowupForm(request.POST or None)
    # If this is a POST request then process the Form data
    if request.method == 'POST'and form.is_valid():

        # Create a form instance and populate it with data from the request (binding):
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
        code = form.cleaned_data['followupcode']
        fol = service.objects.get(id=code)
        results = fol.result
        if not results:
            return HttpResponse("<p> عملیات مورد نظر شما به پایان نرسیده است! </p>")
        res_img = results.result
        postcontext = {
            'res_img' : res_img,
            'code' : code
        }
        return render(request, 'NationalCardFollowup.html', postcontext)

    # If this is a GET (or any other method) create the default form.
    else:
        form = FollowupForm()

    context = {
        'form': form,
    }

    return render(request, 'NationalCardFollowup.html', context)

@login_required
def NationalCardDelivery(request):

    if request.method == 'POST' :
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            address = form.cleaned_data['address']
            date = form.cleaned_data['date']
            deliv = deliveries.objects.create(address=address,date=date)
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
            return redirect('index')

    # If this is a GET (or any other method) create the default form.
    else:
        form = DeliveryForm()

    context = {
        'form': form,
    }


    return render(request, 'NationalCardDelivery.html', context)

@login_required
def Passport(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST' :
        form = PassForm(request.POST, request.FILES)
        if form.is_valid():
            formperimage = form.cleaned_data['perimage']
            formmilitimage = form.cleaned_data['militimage']
            formnatimage = form.cleaned_data['natimage']
            userf = userfile.objects.filter(user=request.user)[0]
            serv = service.objects.create(filenum=userf,typeofservice='Passport',servicedate=datetime.today())
            filesar = files_archive.objects.create(filenum=userf,service=serv,perimage=formperimage,militimage=formmilitimage,natimage=formnatimage)
            messages.info(request, 'کد پیگیری شما ')
            form.save()
            postcontext = {
            'code' : serv.id
            }

            # redirect to a new URL:
            return render(request,'Passport.html',postcontext)


    # If this is a GET (or any other method) create the default form.
    else:
        form = PassForm()

    context = {
        'form': form,
    }

    return render(request, 'Passport.html', context)

@login_required
def PassportFollowup(request):
    form = FollowupForm(request.POST or None)
    # If this is a POST request then process the Form data
    if request.method == 'POST'and form.is_valid():

        # Create a form instance and populate it with data from the request (binding):
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
        code = form.cleaned_data['followupcode']
        fol = service.objects.get(id=code)
        results = fol.result
        if not results:
            return HttpResponse("<p> عملیات مورد نظر شما به پایان نرسیده است! </p>")
        res_img = results.result
        postcontext = {
            'res_img' : res_img,
            'code' : code
        }
        return render(request, 'PassportFollowup.html', postcontext)

    # If this is a GET (or any other method) create the default form.
    else:
        form = FollowupForm()

    context = {
        'form': form,
    }

    return render(request, 'PassportFollowup.html', context)

@login_required
def PassportDelivery(request):

    if request.method == 'POST' :
        form = DeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            address = form.cleaned_data['address']
            date = form.cleaned_data['date']
            deliv = deliveries.objects.create(address=address,date=date)
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
            return redirect('index')

    # If this is a GET (or any other method) create the default form.
    else:
        form = DeliveryForm()

    context = {
        'form': form,
    }

    return render(request, 'PassportDelivery.html', context)

@login_required
def Violation(request):
    if request.method == 'POST':
        form = violationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['ownername']
            carnum = form.cleaned_data['carnum']
            cartype = form.cleaned_data['cartype']
            motornum = form.cleaned_data['motornum']
            policenum = form.cleaned_data['policenum']
            userf = userfile.objects.filter(user=User.objects.filter(username=user)[0])[0]
            viol = violation.objects.create(filenum=userf,policenum=policenum,carnum=carnum,motornum=motornum,cartype=cartype)
    else:
        form = violationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'Violation.html', context)