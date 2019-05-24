from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import CustomerData

# Create your views here.


def index(request):
    form = ContactForm(request.POST)
    context = {
            'form' : form
        }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form' : form
        }
    if form.is_valid():
        newcustomer = form.save()
    
    return render(request, 'landingpage/index.html', context)


    
