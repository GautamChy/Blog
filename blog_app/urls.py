from django.urls import path,include
from rest_framework import routers
from .views import CategoryAPIView,PostAPIView,CommentAPIView

router = routers.DefaultRouter()
router.register(r'categories',CategoryAPIView)
router.register(r'post',PostAPIView)
router.register(r'comments',CommentAPIView)

urlpatterns = [
   
] + router.urls