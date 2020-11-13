from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.username == obj.author.username


# For users to see their info, while no one else can view it
class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.username == obj.username


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

