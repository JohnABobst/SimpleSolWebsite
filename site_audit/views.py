from django.shortcuts import render
from django.views.generic.edit import FormView
from site_audit.forms import AuditRequestForm
from django.views.generic import TemplateView
from django.core.mail import send_mail, get_connection
from exchangelib import *
from exchangelib.items import *


# Create your views here.

class AuditRequestView(FormView):
    template_name = 'audit_request.html'
    form_class = AuditRequestForm
    success_url = '/audit/thanks/'



    def form_valid(self, form):

        form.save()
        return super().form_valid(form)

class ThanksView(TemplateView):
    template_name = 'thanks.html'
