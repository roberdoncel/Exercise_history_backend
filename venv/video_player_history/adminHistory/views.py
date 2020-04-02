from django.shortcuts import render
from django.http import HttpResponse
from adminHistory.models import models, History
import json


# Create your views here.


def save_history(request, urlreceived):
    # Url must be encoded with encodeURIComponent. Ej: encodeURIComponent("https://www.youtube.com/watch?v=2tYeBvAP_0w").
    # Then create a json object and
    # This is necessary to get video param.
    # Example of calling:
    # http://localhost:8000/save_history/https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DuVWkmNgfWmw


    message= {
        "success": 0
    }

    try:
        obj_history = History(url= urlreceived)
        obj_history.save()
        message["success"] = 1
    except:
        message["success"] = 0


    return HttpResponse(json.dumps(message))


def get_history(request):

    message ={}

    try:
        message["result"] = 1
        message["data"] = list(History.objects.values())
    except:
        message["result"] = 0

    return HttpResponse(json.dumps(message))

