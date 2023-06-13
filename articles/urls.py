
from django.urls import path, include
from .views import ArticleViewSet, newArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', ArticleViewSet, basename='articles')
router.register('/<int:pk>/', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
