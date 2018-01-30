from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$', views.ContactRequestView.as_view(), name='contact'),
    url(r'^thanks/', views.ContactThanksView.as_view(), name='contact_thanks')
]
