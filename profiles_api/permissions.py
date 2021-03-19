from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id # """This way this willl return true is the user is trying to update their own profile, otherwise if the id doesnt match, it means that the user is trying to change somebody elses profile, thats why it will return false"""
