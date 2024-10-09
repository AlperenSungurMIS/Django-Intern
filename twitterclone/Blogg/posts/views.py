from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'posts/post_list.html', {'posts': posts, 'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:  # Zaten beğenilmişse beğeniyi kaldır
        like.delete()
    return redirect('post_list')

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()

    return render(request, 'posts/comment_form.html', {'form': form, 'post': post})
