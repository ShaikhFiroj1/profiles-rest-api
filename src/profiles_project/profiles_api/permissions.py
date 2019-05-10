from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to update theri own profile"""

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit thier own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """ Allow user to update theri own statuses"""

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit thier own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
