from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django import forms
from .models import *
from django import forms

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'
