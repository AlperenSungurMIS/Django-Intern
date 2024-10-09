from django.urls import path
from posts.views import post_list, like_post, comment_post


urlpatterns = [
    path('', post_list, name='post_list'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', comment_post, name='comment_post'),  # Yorum URL'si

]
