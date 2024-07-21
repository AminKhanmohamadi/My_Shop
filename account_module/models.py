from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email_active_code = models.CharField(max_length=100 , verbose_name='کد فعال سازی ایمیل')
    about_user = models.TextField(null=True , blank=True , verbose_name='درباره کاربر')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
