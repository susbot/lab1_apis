from rest_framework import permissions


# Base permission class from DRF
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    # To define permissions class, add a has object permission function

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # Check method being made for the request and check if it's on the safe list
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if object being updated matches authenticated user profile
        return obj.id == request.user.id


# Status permission class
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    def has_object_permission(self, request, view, obj):
        """ Check user permissions"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile_id == request.user.id
