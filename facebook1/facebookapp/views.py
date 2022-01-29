from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def facebook(request):

    return render(request,'facebook.html')
