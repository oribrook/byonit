from django.urls import path
from . import api_views

urlpatterns = [        
    path('posts', api_views.serve_all_posts),
    path('post/<str:_id>', api_views.serve_single_post),    
    path('signup', api_views.signup),
    path('post-auth', api_views.serve_auth_post),
]
