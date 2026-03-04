from django.shortcuts import redirect, render, get_object_or_404

from comments.forms import CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', { 'posts': posts }) 

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form': form, 'post': post})

# logica para crear un nuevo post
from .forms import PostForm
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})