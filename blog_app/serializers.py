from rest_framework import serializers
from .models import Category,Post,Comment,Tag

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name',]
        
        
class PostSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','title','body','published_date','is_published','category','tags','author']
        
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','comment','author','created_at']
        
class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']
        
# To make show category name,author name,tags name instead of show category id,author id,tags id .
# class PostSerializers(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     author = serializers.StringRelatedField()
#     tags = serializers.StringRelatedField()
#     class Meta:
#         model = Post
#         fields = '__all__'