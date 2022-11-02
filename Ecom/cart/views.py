from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def signin(request):
    return HttpResponse("this is sign in page")
def login(request):
    return HttpResponse("this is login page")
def about(request):
    return HttpResponse("This is about us page")
def contact(request):
    return HttpResponse("This contact us page")
def loctrac(request):
    return HttpResponse("this is loc tracker page")
def  grieve(request):
    return HttpResponse("this is grievences page")
def  prodview(request):
    return HttpResponse("Your product view will be visible here")

def search(request):
    return HttpResponse("Search Engine brings You here")
def help(request):
    return HttpResponse("Need Any Help")
def offers(request):
    return HttpResponse("These are our offers")