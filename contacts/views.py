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
        form.save() 
        return super().form_valid(form)



class ContactThanksView(TemplateView):
    template_name = 'contact_thanks.html'
