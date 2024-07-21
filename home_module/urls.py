from django.urls import path

from . import views

app_name = 'home_module'


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('site-header/', views.site_header_partial, name='site_header'),

]
