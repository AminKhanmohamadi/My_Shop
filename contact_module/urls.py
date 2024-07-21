from django.urls import path

from . import views
app_name = 'contact_module'
urlpatterns = [
    path('', views.ContactView.as_view() , name='contact_us_page'),

]