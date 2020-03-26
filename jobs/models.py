from django.db import models

# Create your models here.


class Job(models.Model):
    picture = models.ImageField(upload_to='images/' , verbose_name='تصویر')
    summary = models.CharField(verbose_name='توضیحات', max_length=300)