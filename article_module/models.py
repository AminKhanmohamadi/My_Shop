from datetime import timezone

from django.db import models
from account_module.models import User

# Create your models here.
class ArticleCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children' , verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200 ,verbose_name='عنوان')
    url_title = models.CharField(max_length=200, unique=True ,verbose_name='عنوان ادرس')
    is_active = models.BooleanField(default=True , verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'


class Article(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400 , db_index=True , allow_unicode=True , verbose_name='عنوان در url')
    image = models.ImageField(upload_to='article/' , verbose_name='عکس مقاله')
    short_description = models.CharField(max_length=50 , verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال' , default=True)
    selected_categories = models.ManyToManyField(ArticleCategory , verbose_name= 'دسته بندی ها' , related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name='نویسنده' , null=True , editable=False)
    created_at = models.DateTimeField(auto_now_add=True , null=True , blank=True , verbose_name='تاریخ ثبت')
    updated_at = models.DateTimeField(auto_now=True , null=True , blank=True, verbose_name='تاریخ اپدیت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleComment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE ,verbose_name='مقاله')
    parent = models.ForeignKey('self' , on_delete=models.CASCADE , verbose_name='والد' , null=True , blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name='کاربر')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظرات'
        verbose_name_plural = 'لیست نظرات'