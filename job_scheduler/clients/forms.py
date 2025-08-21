from django import forms
from .models import Client, Job

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "email", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter full name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number"
            }),
        }
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["client", "description", "start_date", "finish_date", "status"]
        widgets = {
            "client": forms.Select(attrs={
                "class": "form-control"
            }),  # ✅ Use Select instead of TextInput
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
