from django import forms
from .models import *
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Blog1(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["name","title","content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5, "cols": 50})
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

class Contactus(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'Email', 'comments',"phone"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }