from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    User Specific Permission, requires the user to be the owner of data requested
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
