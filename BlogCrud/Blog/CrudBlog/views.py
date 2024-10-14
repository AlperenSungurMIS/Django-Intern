
from .models import Post

def create_post(title, content):
    post = Post.objects.create(title=title, content=content)
    return post


def list_posts():
    posts = Post.objects.all()
    return posts


def update_post(post_id, title=None, content=None):
    post = Post.objects.get(id=post_id)
    if title:
        post.title = title
    if content:
        post.content = content
    post.save()
    return post


def delete_post(post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
