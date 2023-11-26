from datetime import datetime as dt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import (api_view, authentication_classes, 
                                       permission_classes)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .serializers import PostSerializer
from .models import Post
from django.contrib.auth.models import User


@api_view(['POST'])
def signup(request):
    try:
        username = request.data.get("username", False)
        password = request.data.get("password", False)        
        email = request.data.get("email", "")        

        if not (username and password):
            return Response("missing data. you must specify username & password", 400)
        
        user = User()
        user.username = username
        user.set_password(password)
        user.email = email
        user.save()        
        
        return Response({"info": "user created"}, 200)

    except Exception as e:
        return Response(f"Server error. info: {e}", 500)  # todo: remove info for production
    

@api_view(["POST", "PUT", "DELETE"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def serve_auth_post(request):

    try:
        if request.method == 'POST':            
            title = request.data.get("title", False)
            content = request.data.get("content", False)
            if not (title and content):        
                return Response("Can't create post without title & content", 400)
            
            post = Post()
            post.title = title
            post.content = content
            post.author = request.user
            post.save()            
            return Response(f"Post created. id: {post.id}", 200)                        

        if request.method == "PUT":
            post_id = request.data.get("id", False)            
            post = get_object_or_404(Post, pk=post_id)
            if not post.author == request.user:                
                return Response("Can't modified post which isn't yours!", 400)

            title = request.data.get("title", False)
            content = request.data.get("content", False)
            if not (title or content):        
                return Response("Can't modified post without title or content", 400)            

            post.title = title if title else post.title
            post.content = content if content else post.content
            post.modified = dt.now()
            post.save()

            return Response("Post updated successfully", 200)

        if request.method == "DELETE":
            post_id = request.data.get("id", False)            
            post = get_object_or_404(Post, pk=post_id)
            if not post.author == request.user:
                return Response("Can't delete post which isn't yours!", 400)
            post.delete()
            return Response("Post deleted successfully", 200)
            
    except Exception as e:
        return Response(f"Server error. info: {e}", 500)  # todo: remove info for production


@api_view(['GET'])
def serve_single_post(request, _id):
    post = get_object_or_404(Post, pk=_id)
    return Response(PostSerializer(post).data)


@api_view(['GET'])
def serve_all_posts(request):
    query = Post.objects.all()
    
    # filtering
    created_at = request.GET.get("created_at", False)
    if created_at:
        query = query.filter(created=created_at)

    author = request.GET.get("author", False)
    if author:
        query = query.filter(author__username=author)    

    # sorting
    sort_by = request.GET.get("sort_by", False)
    if sort_by == 'modification':
        query = query.order_by("modified")
    else:    
        # default sorting by created.
        query = query.order_by("created")
            
    return Response(PostSerializer(query.all(), many=True).data)