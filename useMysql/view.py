from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from TestModel import models
import json
from django.shortcuts import get_object_or_404

def hello(request):
    return HttpResponse("Hello world ! ")

def index(request):
    return render(request,'index2.html')

@csrf_exempt
def email_post(request):
    if request.method == 'POST':

        email = request.POST['email']
        e = models.Email(
            email_address = email
        )
        e.save()
        return render(request,'index2.html')

@csrf_exempt
def commit(request):
    if request.method == 'POST':
        servers = request.POST['server']
        opera = request.POST['opera']
        ip = request.POST['ip']
        config = request.POST['config']
        status = request.POST['status']

        p = models.ServerList(
            name = servers,
            ip=ip,
            config=config,
            opera = opera,
            status = status
        )
        p.save()
        return HttpResponse("存储成功")
    else:
        return HttpResponse("存储失败")