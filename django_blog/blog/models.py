from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """Tag model for categorizing posts."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto-populate slug from name when not provided
        from django.utils.text import slugify
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post model representing a blog post.
    
    Fields:
    - title: CharField for the post title
    - content: TextField for the post content
    - published_date: DateTimeField auto-set when created
    - author: ForeignKey to User model
    - tags: ManyToManyField to Tag model
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model for blog post comments.
    
    Fields:
    - post: ForeignKey to Post model
    - author: ForeignKey to User model
    - content: TextField for comment text
    - created_at: DateTimeField auto-set when created
    - updated_at: DateTimeField auto-updated
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
