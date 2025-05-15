from rest_framework import serializers
from .models import Category,Post,Comment

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]
        
        
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','body','published_date','is_published','category','tags','author']
        
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','comment','author','created_at']