from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from comments.forms import CommentForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', { 'posts': posts }) 

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # creado parcialmente
            comment.post = post
            comment.save() # confirma el registro en la BD
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'form': form, 'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post creado correctamente.")
            return redirect('post_create')
        else:
            messages.error(request, "Hubo un error al crear el post.")
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form})
