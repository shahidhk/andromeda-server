from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers

from models import Kadai

def get_kadai(request, kadai_id=None):
    if not kadai_id:
        kadais = Kadai.objects.all()
        jsondata = serializers.serialize("json", kadais)
    else:
        kadai = Kadai.objects.get(pk=int(kadai_id))
        jsondata = serializers.serialize("json", [kadai])
    # print jsondata
    return HttpResponse(jsondata,mimetype='application/json')