from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
import json
import ast
from . import tools 

def run(request):
    print("helllo")
    return render(request, 'mofang.html')

def initState(request):
    if request.method=='POST':
        with open('initState.json', 'r') as f:
            result = json.load(f)
            print(result)
            return HttpResponse(json.dumps(result),content_type="application/json") 

def solve(request):
    if request.method=='POST':
        rev = request.form
        #format rect
        print(rev)
        print("computing...")
        data = rev.to_dict()
        state = []
        data['state'] = ast.literal_eval(data['state'])
        print(data['state'])
        for i in data['state']:
            state.append(int(i))
        result = tools.getResults(state)
        print("complete!")
        return HttpResponse(json.dumps(result),content_type="application/json") 
        



