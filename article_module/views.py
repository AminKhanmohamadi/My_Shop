from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView , ListView
from jalali_date import date2jalali , datetime2jalali
from article_module.models import Article ,ArticleCategory , ArticleComment


# Create your views here.

class ArticleView(ListView):
    model = Article
    template_name = 'article_module/articles_page.html'
    context_object_name = 'articles'



    def get_queryset(self):
        query = super(ArticleView , self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query






class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detial.html'
    context_object_name = 'article_detail'


    def get_queryset(self):
        query = super(ArticleDetailView , self).get_queryset()
        query = query.filter(is_active=True )
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article :Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article_id=article.id ,parent=None).order_by('-created_at').prefetch_related('article__articlecomment_set')
        context['comments_count'] = ArticleComment.objects.filter(article_id=article.id).count()
        return context



def article_categories_component(request):
    article_categories = ArticleCategory.objects.filter(is_active=True)
    context = {'article_categories' : article_categories}

    return render(request , 'article_module/component/article_category_component.html' , context )


def add_article_comment(request):
    if request.user.is_authenticated:
        article_comment = request.GET.get('article_comment')
        article_id = request.GET.get('article_id')
        parent_id = request.GET.get('parent_id')
        print(article_id , article_comment)
        new_comment = ArticleComment(article_id=article_id , text=article_comment , user_id=request.user.id , parent_id=parent_id)
        new_comment.save()
        context = {'comments': ArticleComment.objects.filter(article_id=article_id , parent=None).order_by('-created_at').prefetch_related('article__articlecomment_set'),
                   'comments_count': ArticleComment.objects.filter(article_id=article_id ).count()}
        return render(request , 'article_module/inc/article_comment_partial.html' , context)

    return HttpResponse('response')
