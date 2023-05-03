from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import filters

from api.mixins.permission_by_action import PermissionByAction
from api.paginations import StandardPagination
from api.permissions import IsOwner
from api.serializers import PostSerializer
from post.models import Post


class PostModelViewSet(PermissionByAction, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_by_action = {
        'create': (IsAuthenticated,),
        'update': (IsAuthenticated, IsOwner,),
        'destroy': (IsAuthenticated, IsOwner,),
        'retrieve': (AllowAny,),
        'list': (AllowAny,),
    }
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
