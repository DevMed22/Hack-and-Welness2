from django.urls import path
from .views import (PostsListView, CreatePost, UpdatePost,
                     PostDetail, DeletePost)
app_name = "posts"    


urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('create/', CreatePost.as_view(), name='create_post'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit/', UpdatePost.as_view(), name='update_post'),
    path('<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),
]