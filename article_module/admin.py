from django.contrib import admin
from .models import Article , ArticleCategory , ArticleComment
# Register your models here.
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'url_title' , 'parent' , 'is_active')
    list_editable = ['url_title' , 'parent' ,'is_active']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'is_active' , 'author')
    list_editable = ['is_active']

    def save_model(self, request, obj:Article , form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj ,form, change)


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('user' , 'article' , 'created_at' , 'parent')

