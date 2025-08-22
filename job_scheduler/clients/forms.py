from django import forms
from .models import Client, Job

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "address", "email", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Client's Name"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Client's Address"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Email Address"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Phone Number"
            }),
        }
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["client", "description", "start_date", "finish_date", "status"]
        widgets = {
            "client": forms.Select(attrs={
                "class": "form-control"
            }),  
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Job description"
            }),
            "start_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            "finish_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            "status": forms.Select(attrs={
                "class": "form-control"
            }),
        }
