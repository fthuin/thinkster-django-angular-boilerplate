from rest_framework import permissions


class IsParticipantOfTricount(permissions.BasePermission):
    def has_object_permission(self, request, view, tricount):
        if request.user:
            return request.user is in tricount.participants
        return False
