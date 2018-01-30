from django import forms
from site_audit.models import AuditRequest
from django.forms import ModelForm
from django.db import models

class AuditRequestForm(forms.ModelForm):
    class Meta:
        model = AuditRequest
        fields = "__all__"
