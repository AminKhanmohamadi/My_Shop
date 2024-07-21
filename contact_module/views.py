from django.shortcuts import render , redirect
from .forms import  ContactUsForm
from django.contrib import messages
from django.views import View
from django.views.generic.edit import FormView ,CreateView
from .models import *
from site_module.models import SiteSetting
# Create your views here.

class ContactView(CreateView):
   form_class = ContactUsForm
   template_name = 'contact_module/contact_us_page.html'
   success_url = '/contact-us/'

   def get_context_data(self, *args ,**kwargs):
      context = super().get_context_data(*args , **kwargs)
      setting = SiteSetting.objects.filter(is_main_setting=True).first()
      context['site_setting'] = setting
      return context



