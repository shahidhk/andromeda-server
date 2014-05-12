from django.shortcuts import render
from django.http import HttpResponse
import json

def get_data(request):
    jsondata = {}
    return HttpReponse(jsondata,mimetype='application/json')