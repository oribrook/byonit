from rest_framework import serializers 
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username"]


class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    class Meta:
        model = Post
        fields = "__all__"
