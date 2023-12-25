from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import ConatctViwe
def index(request):
    return render(request,'index.html')

def components(request):
    return render(request,'components.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        data=ConatctViwe.objects.create(name=name,email=email,message=message)

        return redirect('index')