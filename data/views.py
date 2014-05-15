from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core import serializers
from forms import KadaiForm

from models import Kadai
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_kadai(request, kadai_id=None):
    if request.method == "POST":
        data = request.POST.copy()
        print data
        kadaiform = KadaiForm(request.POST, request.FILES)
        if kadaiform.is_valid():
            kadai = kadaiform.save()
            jsondata = serializers.serialize('json', [kadai])
    elif not kadai_id:
        kadais = Kadai.objects.all()
        jsondata = serializers.serialize("json", kadais)
    else:
        kadai = Kadai.objects.get(pk=int(kadai_id))
        jsondata = serializers.serialize("json", [kadai])
    # print jsondata
    return HttpResponse(jsondata,mimetype='application/json')