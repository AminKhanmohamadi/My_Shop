from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Product, ProductCategory
from django.views.generic import ListView, DetailView
from django.views import View


# Create your views here.

class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['category']
    paginate_by = 2

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        category = self.kwargs.get('category')
        if category is not None:
            base_query =base_query.filter(category__url_title__iexact=category)
        return base_query




class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('product_favorite')
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context



class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = get_object_or_404(Product, pk=product_id)
        request.session['product_favorite'] = product_id
        return redirect(product.get_absolute_url())






def product_category(request):
    category_list = ProductCategory.objects.filter(is_active=True , parent_id=None)
    context = {'category_list': category_list}

    return render(request , 'product_list_category.html' , context)

