from django.shortcuts import render
from django.views.generic.edit import FormView
from site_audit.forms import AuditRequestForm
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

class AuditRequestView(FormView):
    template_name = 'audit_request.html'
    form_class = AuditRequestForm
    success_url = '/audit/thanks/'



    def form_valid(self, form):
        # subject = ''
        # for k in form.cleaned_data:
        #     subject += k.replace("_", " ") + ' = ' + form.cleaned_data[k] + '\n'
        # send_mail(
        # "You have a new site audit request",
        # subject,
        # settings.EMAIL_HOST_USER,
        # ['scheduling@simplesol.com', 'sales@simplesol.com'],
        # fail_silently = False
        #
        # )

        form.save()
        return super().form_valid(form)

class ThanksView(TemplateView):
    template_name = 'thanks.html'
