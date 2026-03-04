# Integración con User de Django

## Cambios realizados

### 1. Modelos

#### `blog/models.py`
- Cambiado `author = CharField(max_length=100)` por `author = ForeignKey(User, on_delete=models.CASCADE)`

#### `comments/models.py`
- Cambiado `author = CharField(max_length=100)` por `author = ForeignKey(User, on_delete=models.CASCADE)`
- Agregado import: `from django.contrib.auth.models import User`

### 2. Forms

#### `comments/forms.py`
- Removido campo `author` del form (ya no es necesario, se usa el usuario autenticado)
- Ahora solo acepta `content`

### 3. Views

#### `blog/views.py`
- `post_create`: Se asigna `request.user` como autor del post antes de guardar
- `post_detail`: Se asigna `request.user` como autor del comentario antes de guardar

### 4. Migraciones creadas
- `blog/migrations/0003_alter_post_author.py`
- `comments/migrations/0002_alter_comments_author.py`

---

## Uso

- Los usuarios deben estar autenticados para crear posts y comentarios
- Los posts y comentarios muestran `post.author.username` en templates
- Para aplicar los cambios en la base de datos: `python manage.py migrate`
