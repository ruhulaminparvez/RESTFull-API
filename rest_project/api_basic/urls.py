from re import A
from django.urls import path
from .views import ArticleAPIView, ArticleDetailView

urlpatterns = [
    
    # path('article/', article_list, name="article"),
    # path('detail/<int:pk>/', article_detail, name="detail"),

    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
] 