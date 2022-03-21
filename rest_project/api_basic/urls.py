from re import A
from django.urls import path, include
from .views import ArticleAPIView, ArticleDetailView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    
    # path('article/', article_list, name="article"),
    # path('detail/<int:pk>/', article_detail, name="detail"),

    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:pk>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
] 