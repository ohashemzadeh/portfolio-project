from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    pub_date = models.DateTimeField(verbose_name='تاریخ انتشار')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(verbose_name='تصویر', upload_to='images/')

    def body_summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.title