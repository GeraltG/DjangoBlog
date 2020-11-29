from django.shortcuts import get_object_or_404, render

# Create your views here.
from blog.models import Blog, BlogType


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()  # get all blogs
    context['blogs_count'] = Blog.objects.all().count()  # count blog's number
    return render(request, "blog_list.html", context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=blog_pk)  # id->primary key
    return render(request, 'blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blogs_count'] = Blog.objects.filter(blog_type=blog_type).count()
    context['blog_types'] = blog_type
    return render(request, "blogs_with_type.html", context)

