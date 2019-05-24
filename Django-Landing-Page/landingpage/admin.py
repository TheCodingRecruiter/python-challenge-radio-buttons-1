from django.contrib import admin
from .forms import ContactForm
from .models import CustomerData
# Create your models here.

admin.site.register(CustomerData)

