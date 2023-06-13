
from django.urls import path, include
from .views import ArticleViewSet, UserViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

router.register('users', UserViewset, basename='articles')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
