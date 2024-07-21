from django.db import models

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=300 , verbose_name='موضوع پیام')
    email = models.EmailField(max_length=300 , verbose_name='پست الکترونیک')
    full_name = models.CharField(max_length=300 , verbose_name='نام ونام خانوادگی')
    message= models.TextField(verbose_name='متن پیام')
    created_date = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ایجاد')
    response = models.TextField(verbose_name='پاسخ تماس با ما' , null=True , blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین' , default=False)

    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='لیست تماس با ما'

    def __str__(self):
        return self.title