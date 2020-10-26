from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
import json

def run(request):
    print("helllo")
    return render(request, 'mofang.html')

def initState(request):
    if request.method=='POST':
        with open('initState.json', 'r') as f:
            result = json.load(f)
            return  