from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, instance):
        return instance.author == request.user or request.user.is_superuser