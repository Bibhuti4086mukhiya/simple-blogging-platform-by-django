from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
from django.template.defaultfilters import date
from django.utils.text import slugify

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_authors')
    body = HTMLField()
    excerpt = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="pics", null=True, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    @property
    def published(self):
        return '%s' % date(self.publish, "F d, Y")
    
    @property
    def comments(self):
        return Comment.objects.filter(post= self.id).order_by('-id')
    
    @property
    def related_posts(self):
        return Post.objects.filter(category = self.category).exclude(id=self.pk)[:6]
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentator')
    text = models.CharField(max_length=500, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    