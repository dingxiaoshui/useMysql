from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from TestModel import models
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect
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
@csrf_exempt
def search_form(request):
    return render(request,'search_form.html')

@csrf_exempt
def search(request):
    error = False
    if 'q' in request.GET:
        s = request.GET['q']
        if not s:
            error = True
        else:
            server = models.ServerList.objects.get(name=s)
            return render(request,'search.html',{'server':server})
    return render(request, 'search_form.html', {'error': error})

# @csrf_exempt
# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST['subject']:
#             errors.append('Enter a subject:')
#         if not request.POST['message']:
#             errors.append('Enter a message:')
#         if not request.POST['email'] and '@' not in request.method.POST.get['email']:
#             errors.append('Enter a valid email')
#         if not errors:
#
#             return HttpResponseRedirect('/contact/thanks/')
#
#     return render(request,'contact_form.html',{'errors':errors})

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(
            initial = {'subject': 'I love your site!'}
        )
    return render_to_response('contact_form.html',{'form':form})


