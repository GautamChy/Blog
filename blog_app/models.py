from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
      
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.title}| {self.author}| {self.published_date}| {self.category.name} | {self.is_published}"
    
class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return f" Commented by {self.author.username} on {self.post.title} : {self.comment}| {self.created_at}"