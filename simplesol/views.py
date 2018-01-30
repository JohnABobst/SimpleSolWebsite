from django.views.generic import TemplateView

class LandingPage(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name= 'about.html'

# class Contact(TemplateView):
#     template_name = 'contact.html'

class Guarantee(TemplateView):
    template_name = 'guarantee.html'

class Services(TemplateView):
    template_name = "services.html"

class CyberSecurity(TemplateView):
    template_name = "cybersecurity.html"

class Testing(TemplateView):
    template_name = "testing.html"
