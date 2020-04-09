from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
    allblogs = Blog.objects
    return render(request, 'allblogs/allblogs.html', {'blogs':allblogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'allblogs/detail.html', {'blog': detailblog})
