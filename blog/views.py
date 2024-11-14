from django.shortcuts import render
from .models import blog

# Create your views here.

def all_blogs(request):
    blog_ = blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blog':blog_})
