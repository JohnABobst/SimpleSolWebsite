from django.shortcuts import render
from django.views.generic.edit import FormView
from contacts.forms import ContactForm
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings

class ContactRequestView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/contact/thanks/'




    def form_valid(self, form):
        subject = ''
        for k in form.cleaned_data:
            subject += k.replace("_", " ") + ' = ' + form.cleaned_data[k] + '\n'
        send_mail(
        "You have a new contact request",
        subject,
        settings.EMAIL_HOST_USER,
        ['scheduling@simplesol.com', 'sales@simplesol.com'],
        fail_silently = False

        )

        form.save()
        return super().form_valid(form)



class ContactThanksView(TemplateView):
    template_name = 'contact_thanks.html'
