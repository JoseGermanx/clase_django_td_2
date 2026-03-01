
# Formulario para crear un nuevo comentario
from .models import Comments

from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

        