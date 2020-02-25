from rest_framework import permissions


class UserProfilePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # it is list
            return True

        return obj.id == request.user.id


class OwnFeedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # it is list
            return True
        return obj.user_profile_id == request.user.id
