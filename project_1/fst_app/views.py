from django.shortcuts import render


from django.http import HttpResponse 

def seller(request):
    return HttpResponse("Bro,This is seller page");

def Buyer(request):
    return HttpResponse("Bro,This is buyer page");


def home(request):
    return HttpResponse("Bro,This is fst_app home page");