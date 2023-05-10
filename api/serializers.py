from rest_framework import serializers

from api.auth.serializers import UserSerializer
from post.models import Post


class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer(many=False)

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):

        previous_result = super().to_representation(instance)

        print(previous_result)

        return previous_result
