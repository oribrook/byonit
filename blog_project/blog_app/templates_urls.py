from django.urls import path
from . import views 


urlpatterns = [        
    path('posts', views.serve_all_posts),
    path('post/<int:_id>', views.serve_single_post),
]
