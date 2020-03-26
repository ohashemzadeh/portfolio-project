from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from .views import *

app_name = 'blog'
urlpatterns = [

    path('blog_list', blog_list , name='blog_list'),
    path('blog_details/<int:blog_id>', blog_details , name='blog_details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)