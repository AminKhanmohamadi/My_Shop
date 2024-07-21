from django.urls import path
from .views import *
app_name = 'article_module'

urlpatterns = [

    path('' , ArticleView.as_view() , name='article_page'),
    path('cat/<str:category>' , ArticleView.as_view() , name='article_by_category'),
    path('<int:pk>/' , ArticleDetailView.as_view() , name='article_detail_page'),
    path('add-article-comment' , add_article_comment , name='add_article_comment'),


]