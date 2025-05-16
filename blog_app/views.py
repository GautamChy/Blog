from django.shortcuts import render
from .models import Category,Post,Comment,Tag
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializers,PostSerializers,CommentSerializers,TagSerializers
from rest_framework.pagination import  PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter


# Create your views here.
class CategoryAPIView(ModelViewSet):
    
    #queryset = Category.objects.select_related() # To reduce time with the help of debug_tool_bar
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
    # modify pagination
class Pages(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
class PostAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = Pages
    filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
    filterset_fields = ('published_date',)
    search_fields = ['id','title','category__name','author__username']
    
    
    # Modify pagination 
class Pages(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    pagination_class = PageNumberPagination
    pagination_class = Pages
    

 # Default pagination 
class TagAPIView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    pagination_class = PageNumberPagination

    
        
    

    
    
    
