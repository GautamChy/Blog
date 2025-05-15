from django.contrib import admin
from .models import Category,Post,Comment,Tag

# Register your models here.

admin.site.site_title = "Blog Admin Portal"
admin.site.site_header = "Blog Admin"
admin.site.index_title = "Welcome to Blog Platform with Commenting System"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    list_filter = ('name',)
admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','body','published_date','is_published','category','author')
    search_fields = ('title','author__username','category__name')
    list_filter = ('published_date',)
    list_per_page = 10
admin.site.register(Post,PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')
    list_filter = ('name',)
admin.site.register(Tag,TagAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','author','post','comment','created_at')
    list_per_page = 10
    list_filter = ('created_at',)
    
admin.site.register(Comment,CommentAdmin)

