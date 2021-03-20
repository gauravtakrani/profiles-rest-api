from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id # """This way this willl return true is the user is trying to update their own profile, otherwise if the id doesnt match, it means that the user is trying to change somebody elses profile, thats why it will return false"""


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True #

        return obj.user_profile.id == request.user.id #if user id and feed user match, this will return true.
        #We used the above return statement for put patch or delete methods, i.e. not safe methods
