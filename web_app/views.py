from multiprocessing import context
from django.shortcuts import render,HttpResponse

from web_app.models import Index

# Create your views here.

def index(request):
    
    if request.method == 'POST':
            index = Index()
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            index.name=name
            index.email=email
            index.subject=subject
            index.message=message
            index.save()
    return render(request,"index.html")