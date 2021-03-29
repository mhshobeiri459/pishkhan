from django.urls import path
from pishkhanapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('DrivingLiscense/', views.DrivingLiscense, name='DrivingLiscense'),
    path('DrivingLiscenseFollowup/', views.DrivingLiscenseFollowup, name='DrivingLiscenseFollowup'),
    path('DrivingLiscenseDelivery/', views.DrivingLiscenseDelivery, name='DrivingLiscenseDelivery'),
    path('NationalCard/', views.NationalCard, name='NationalCard'),
    path('NationalCardFollowup/', views.NationalCardFollowup, name='NationalCardFollowup'),
    path('NationalCardDelivery/', views.NationalCardDelivery, name='NationalCardDelivery'),
    path('Passport/', views.Passport, name='Passport'),
    path('PassportFollowup/', views.PassportFollowup, name='PassportFollowup'),
    path('PassportDelivery/', views.PassportDelivery, name='PassportDelivery'),
    path('signup/', views.signup, name='signup'),
    path('Violation/', views.Violation, name='Violation'),




]
