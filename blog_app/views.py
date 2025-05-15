from django.shortcuts import render
from .models import Category,Post,Comment
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializers,PostSerializers,CommentSerializers


# Create your views here.
class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
class PostAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    

    
    
    
