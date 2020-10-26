from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
import json
import ast
from . import tools 

def run(request):
    return render(request, 'mofang.html')

def initState(request):
    if request.method=='POST':
        with open('initState.json', 'r') as f:
            result = json.load(f)
            return HttpResponse(json.dumps(result),content_type="application/json") 

def solve(request):
    if request.method=='POST':
        print("computing...")
        state = []
        # print(request.POST.get("state"))
        # for i in data['state']:
        for i in ast.literal_eval(request.POST.get("state")):
            state.append(int(i))
        result = tools.getResults(state)
        print("complete!")
        return HttpResponse(json.dumps(result),content_type="application/json") 
        



