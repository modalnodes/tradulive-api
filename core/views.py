from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .serializers import *

import dateutil.parser

import json

def update_field(request):
    t = request.GET.get("t")
    i = request.GET.get("i")
    f = request.GET.get("f")
    v = request.GET.get("v")
    
    ts = {
        'translator':TranslatorProfile
    }
    
    itm = ts[t].objects.get(pk=i)
    setattr(itm, f, v)
    itm.save()
    
    return HttpResponse(json.dumps({"response":"OK"}))
    
    
def search(request):
    f = request.GET.get("from")

    t = request.GET.get("to")

    d = request.GET.get("date")
    d = dateutil.parser.parse(d)
    d = d.date()
    
    ts = TranslatorProfile.objects.filter(
        languages__language_from__name=f, 
        languages__language_to__name=t, 
        availabilities__dow=d.isoweekday(),
        exceptions__date_from__lte=d,
        exceptions__date_to__gte=d
        )
    
    return HttpResponse(json.dumps(TranslatorProfileSerializer(ts, many=True).data))