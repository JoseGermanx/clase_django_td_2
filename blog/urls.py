
from django.urls import path, include
from .views import post_list, post_detail, post_create, profile, EditorView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('post/', post_create, name='post_create'),
    path('perfil/', profile, name='profile'),
    path('editor/', EditorView.as_view(), name='editor'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]