from rest_framework import serializers

from api.auth.serializers import UserSerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer(many=False)

    class Meta:
        model = Post
        fields = '__all__'