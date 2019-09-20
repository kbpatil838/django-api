import socket
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import os
import subprocess
import psutil
import platform
import requests


@api_view(['GET'])
def ip(ip):
    l = {}
    ipaddress = ip.META["REMOTE_ADDR"]
    l['ip_address'] = ipaddress
    return JsonResponse(l, safe=False)


def host(host):
    a = host.get_host()
    h = {}
    h['host_address']=a
    return JsonResponse(h, safe=False)


def cpu(request):
    cpu1=psutil.cpu_percent()
    cpu1=str(cpu1)
    c={}
    c["cpu_usage_in_percent"]=cpu1
    return JsonResponse(c, safe=False)


def machine_platform(request):
    pl= platform.machine()
    p={}
    p['plateform']=pl
    return JsonResponse(p, safe=False)


def vmem(request):
    mem1=psutil.virtual_memory()
    mem1=str(mem1)
    return JsonResponse(mem1, safe=False)


def os_information(request):
    osinf1=os.uname()
    return JsonResponse(osinf1, safe=False)


def disk_storage(request):
    obj_Dis1 = psutil.disk_usage('/')
    obj_Dis1=str(obj_Dis1)
    obj_D=obj_Dis1.split() 
    return JsonResponse(obj_D, safe=False)


def device_mount(request):
    dev= subprocess.check_output('findmnt', shell=True)
    d=[]
    d.append(dev.split('\n'))
    #mount=json.dumps(d)
    return JsonResponse(d, safe=False)


def process_running(request):
    process= subprocess.check_output('ps', shell=True)
    p=[]
    p.append(process.split('\n'))
    #process=json.dumps(p)
    return JsonResponse(p, safe=False)  


def Netstat_info(request):
     nets= subprocess.check_output('netstat', shell=True)
     n=[]
     n.append(nets.split('\n'))
     n=json.dumps(n)
     return JsonResponse(n, safe=False)