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

# Create your views here.
def index(request):
    return render(request, "index.html", {})


class violationListView(ListView):
    model = violation
    template_name = "Violation.html"


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def DrivingLiscense(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = baseForm(request.POST)
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        res = resultreq.objects.create(result='results/accepted.png')
        userf = userfile.objects.filter(user=request.user)[0]
        serv = service.objects.create(result=res,filenum=userf,typeofservice='DrivingLiscense',servicedate=datetime.today())
        # redirect to a new URL:
        return HttpResponseRedirect(reverse('') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = baseForm()

    context = {
        'form': form,
    }

    return render(request, 'DrivingLiscense.html', context)

@login_required
def DrivingLiscenseFollowup(request):
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

    form = FollowupForm(request.POST or None)
    # If this is a POST request then process the Form data
    if request.method == 'POST'and form.is_valid():
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
        return HttpResponseRedirect(reverse('') )

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
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = baseForm(request.POST)
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        res = resultreq.objects.create(result='results/accepted.png')
        userf = userfile.objects.filter(user=request.user)[0]
        serv = service.objects.create(result=res,filenum=userf,typeofservice='NationalCard',servicedate=datetime.today())
        # redirect to a new URL:
        return HttpResponseRedirect(reverse('') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = baseForm()

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

    form = FollowupForm(request.POST or None)
    # If this is a POST request then process the Form data
    if request.method == 'POST'and form.is_valid():
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
        return HttpResponseRedirect(reverse('') )

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
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = baseForm(request.POST)
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        res = resultreq.objects.create(result='results/accepted.png')
        userf = userfile.objects.filter(user=request.user)[0]
        serv = service.objects.create(result=res,filenum=userf,typeofservice='Passport',servicedate=datetime.today())
        # redirect to a new URL:
        return HttpResponseRedirect(reverse('') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = baseForm()

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

    # If this is a POST request then process the Form data
    form = DeliveryForm(request.POST or None)
    # If this is a POST request then process the Form data
    if request.method == 'POST'and form.is_valid():
        # Check if the form is valid:
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
        # redirect to a new URL:
        return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = DeliveryForm()

    context = {
        'form': form,
    }

    return render(request, 'PassportDelivery.html', context)