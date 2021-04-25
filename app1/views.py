from django.http.response import HttpResponse
from django.shortcuts import render
import os
# Create your views here.

def home(request):
    return HttpResponse("hihhihih"+str(os.environ.get('ID')))