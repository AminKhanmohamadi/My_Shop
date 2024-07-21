from django.urls import path
from . import views

app_name = 'product_module'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('category/<str:category>/', views.ProductListView.as_view(), name='product-category'),
    path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-favorite/', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),


]