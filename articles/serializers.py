from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }

        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user
