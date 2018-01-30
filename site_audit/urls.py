from django.conf.urls import url
from django.contrib import admin
from . import views


app_name='site_audit'

urlpatterns = [
    url(r'^$',views.AuditRequestView.as_view(), name='audit'),
    url(r'^thanks/', views.ThanksView.as_view(), name='thanks'),
]
