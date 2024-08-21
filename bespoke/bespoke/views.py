from django.shortcuts import render
from django.http import HttpResponse
def bespoke(request):
    return render(request, "bespoke/bespokepage.html")

def contactus(request):
    return render(request, 'bespoke/contactus.html')

def book(request):
    return render(request, 'bespoke/book.html')