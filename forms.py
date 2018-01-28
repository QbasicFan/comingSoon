from django import forms
from .models import eMail


class eMailForm(forms.ModelForm):
    class Meta:
        model = eMail
        fields = ['name','email','message']
