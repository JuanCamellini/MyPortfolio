from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
