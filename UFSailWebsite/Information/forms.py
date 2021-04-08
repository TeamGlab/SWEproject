from django import forms
from .models import EmailMember

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailMember
        fields = ["email"]
