from django.shortcuts import render
from django.views.generic.edit import FormView
from contacts.forms import ContactForm
from django.views.generic import TemplateView
from exchangelib import *
from exchangelib.items import *

class ContactRequestView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/contact/thanks/'


    def form_valid(self, form):
        credentials = Credentials(
            username='simplesol.com\\jbobst',
            password='Pa55word!'
        )
        account = Account(
            primary_smtp_address='jbobst@simplesol.com',
            credentials=credentials,
            autodiscover=True,
            access_type=DELEGATE
            )
        audit_request = ''
        for k in form.cleaned_data:
            audit_request += k + ' = ' + form.cleaned_data[k] + '\n'

        m = Message(
           account=account,
           subject='You have a new site audit request',
            body= audit_request,
            to_recipients=['sales@simplesol.com','scheduling@simplesol.com'],
            )

        m.send_and_save()

        form.save()
        return super().form_valid(form)



class ContactThanksView(TemplateView):
    template_name = 'contact_thanks.html'
