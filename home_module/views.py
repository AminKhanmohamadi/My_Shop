from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from product_module.models import Product , ProductCategory
from site_module.models import SiteSetting
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home_module/index_page.html'



def SiteHeaderComponent(request):
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    category = ProductCategory.objects.all()

    context = {
        'site_setting': site_setting,
        'category': category

    }
    return render(request , 'shared/site_header_component.html' , context)



def SiteFooterComponent(request):
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()

    context = {
        'site_setting': site_setting,

    }
    return render(request , 'shared/site_footer_component.html' , context)





def product_categories_component(request):
    product_category = ProductCategory.objects.filter(is_active=True)
    context = {'product_categories' : product_category}

    return render(request , 'home_module/component/category_all.html' , context )



