from django.shortcuts import render, get_object_or_404
from .models import Post


def serve_all_posts(request):
    posts = list(Post.objects.all())
    return render(request=request, template_name="blog_app/index.html", context={"posts": posts})


def serve_single_post(request, _id):    
    posts = get_object_or_404(Post, pk=_id)
    return render(request=request, template_name="blog_app/index.html", context={"posts": [posts]})
    
