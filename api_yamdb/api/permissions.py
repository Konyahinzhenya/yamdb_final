from rest_framework.permissions import (BasePermission, SAFE_METHODS,
                                        IsAuthenticatedOrReadOnly)


class IsAdmin(BasePermission):
    """Разрешения api от имени администратора."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin
            or request.user.is_staff
            or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return request.method in ('GET', 'POST', 'PATCH', 'DELETE')


class IsAdminOrReadOnly(BasePermission):
    """Доступ к title, genre и category."""
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
            or request.user.is_superuser
        )


class MePermission(BasePermission):
    """Разрешения действий с пользователями для юзеров."""
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, view, request, obj):
        return request.method in ('PATCH', 'GET')


class ReviewPermission(IsAuthenticatedOrReadOnly):
    """доступ для авторов, админов и модераторов для коментов и отзывов"""
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
            or request.user.is_authenticated
            and request.user.is_moderator
        )
