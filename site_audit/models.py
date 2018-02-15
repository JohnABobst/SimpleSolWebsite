from django.db import models

# Create your models here.

class AuditRequest(models.Model):
    contact_name = models.CharField(max_length = 100)
    company_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    contact_number = models.CharField(max_length=50)
    contact_email = models.EmailField()
    company_URL = models.CharField(max_length = 256)
    Tell_Us_About_Your_Needs = models.TextField()

    def __str__(self):
        return self.company_name
