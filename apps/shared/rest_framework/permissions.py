from rest_framework.permissions import BasePermission, DjangoModelPermissions


class IsSaveMethod(BasePermission):
    save_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS']

    def has_permission(self, request, view):
        return request.method in self.save_methods


class IsAuthenticated(IsSaveMethod):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and
                super(IsAuthenticated, self).has_permission(request, view))


class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.add_%(model_name)s']


class IsAdminOrStaffOrSelfForUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method not in ['POST', 'PATCH', 'PUT']:
            return IsAuthenticated.has_permission(IsAuthenticated.__call__(), request, view)

        user = request.user
        user_roles = user.role.all().values_list('unique_name', flat=True)

        if 'admin' in user_roles or request.user.is_staff:  # Админ или суперюзер
            return True
        return obj.id == request.user  # Свой
