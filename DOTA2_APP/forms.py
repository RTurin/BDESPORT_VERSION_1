from django import forms
from django.forms.widgets import TextInput
from .models import *



class Register_Team_Form(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'shortname',
            'logo',
        ]
