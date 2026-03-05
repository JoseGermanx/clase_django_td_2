from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', { 'posts': posts }) 

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # creado parcialmente
            comment.post = post
            comment.author = request.user
            comment.save() # confirma el registro en la BD
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'form': form, 'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post creado correctamente.")
            return redirect('post_create')
        else:
            messages.error(request, "Hubo un error al crear el post.")
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def profile(request):
    posts = Post.objects.filter(author_id=request.user)
    return render(request, 'blog/profile.html', {'posts': posts})


class EditorView(PermissionRequiredMixin, TemplateView):
    template_name='blog/editor.html'
    permission_required='blog.change_post'
    raise_exception = True