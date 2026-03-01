
from django.urls import path, include
from .views import post_list, post_detail, post_create

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('post/', post_create, name='post_create'),

]