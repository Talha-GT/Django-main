from django.http import HttpResponse 

def contact(request):
    return HttpResponse("This is contact page");

def home(request):
    return HttpResponse(" Bro, This is Home page");

def talha(request):
    return HttpResponse("Hey Talha Bro Whats about you");