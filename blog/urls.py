from django.urls import path
from .views import ArticleList, ArticleDetail, DetailList

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="detail"),
    path('category/<slug:slug>', DetailList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>', DetailList.as_view(), name="category"),
]
