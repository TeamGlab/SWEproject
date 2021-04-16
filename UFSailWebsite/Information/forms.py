from django import forms
from django.forms import Textarea, TextInput, EmailInput
from .models import EmailMember


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailMember
        fields = ['email']
        widgets = {'email': EmailInput(attrs={'style': 'margin-left : 10px'})}

