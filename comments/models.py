from django.db import models
from blog.models import Post

# Create your models here.

# Cada post puede tener muchos comentarios y 1 comentario pertenece a un Post

class Comments(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.post.title}'
