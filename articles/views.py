from .serializers import *
from .models import Article
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    queryset = Article.objects.all()
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
