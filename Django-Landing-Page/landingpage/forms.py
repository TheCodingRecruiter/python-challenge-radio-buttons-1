from django.forms import ModelForm
from django import forms
from .models import CustomerData

MONTH_CHOICES = [
    ('January', 'January'),
    ('February', 'February'),
    ('March','March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June','June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December')
]

class ContactForm(ModelForm):
    month = forms.ChoiceField(choices=MONTH_CHOICES, widget=forms.RadioSelect())
    phone = forms.CharField(required=False)
    class Meta:
        model = CustomerData
        fields = ['firstname', 'lastname', 'npo', 'email', 'phone', 'month']
