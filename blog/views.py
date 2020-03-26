from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.


def blog_list(request):
    template_name = 'blog/blog_list.html'
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, template_name, context)


def blog_details(request, blog_id):
    template_name = 'blog/blog_details.html'
    blog = get_object_or_404(Blog, pk=blog_id)
    print(blog)
    context = {'blog': blog}
    return render(request, template_name, context)