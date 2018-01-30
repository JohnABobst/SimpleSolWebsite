from django import forms
from contacts.models import Contacts
from django.forms import ModelForm
from django.db import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"
