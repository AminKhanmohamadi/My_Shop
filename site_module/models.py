from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')
    site_name = models.CharField(max_length=200 , verbose_name='نام سایت')
    address = models.CharField(max_length=200 , verbose_name='ادرس ')
    phone = models.CharField(max_length=200,null=True , blank=True , verbose_name='تلفن سایت')
    fax = models.CharField(max_length=200 , null=True, blank=True,verbose_name='فکس سایت')
    email = models.CharField(max_length=200 ,null=True ,blank=True, verbose_name='ایمیل سایت')
    copy_right = models.TextField( verbose_name='کپی رایت سایت')
    site_ulr = models.CharField(max_length=200 ,verbose_name='دامنه سایت')
    about_us_text = models.TextField(verbose_name='توضیحات سایت')
    site_logo = models.ImageField(upload_to='site-settings/' , verbose_name='لوگوی سایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class Slider(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان')
    url = models.CharField(max_length=200 , verbose_name='لینک')
    url_title = models.CharField(max_length=200 , verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='sliders/' , verbose_name='تصویر اسلایدر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title