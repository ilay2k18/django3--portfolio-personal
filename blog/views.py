from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
# To limit no of objects in a blog to 5 with recent date
#    blogs = Blog.objects.order_by('date')[:5]

    return render(request, 'blog/all_blogs.html',{'blogs':blogs})
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})