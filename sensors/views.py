"""# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here."""
from django.shortcuts import render,get_object_or_404
from .models import Sensors
from django.http import HttpResponse
from django.forms.models import model_to_dict
def aaa(request):
	"""all_sensors = Sensors.objects.all()"""
	all_sensors = Sensors.objects.get(pk=Sensors.objects.count())
	return render(request ,'sensors/aaa.html',{'all_sensors':all_sensors})
	#return HttpResponse(template.render(context,request))


def Display(request,temperature=None,humidity=None,ps1=None,as1=None,as2=None,ps2=None,wl=None):
    all_sensors = Sensors()
    #all_sensors = Sensors.objects.all()
    #if (sensor1 != None):
    all_sensors.temperature=float(temperature)
    all_sensors.humidity=float(humidity)
    all_sensors.ps1=float(ps1)
    all_sensors.ps2=float(ps2)
    all_sensors.wl=float(wl)
    all_sensors.as1=str(as1)
    all_sensors.as2=str(as2)
    all_sensors.save()
    return render(request ,'sensors/sensors.html',{'all_sensors':all_sensors})
	#return render(request ,'sensors/detail.html',{'all_sensors':all_sensors})"""
def new_disp(request):
    all_sensors = Sensors.objects.get(pk=Sensors.objects.count())
    #print(all_sensors.temperature)
    return render(request ,'sensors/sensors.html',{'all_sensors':all_sensors})


