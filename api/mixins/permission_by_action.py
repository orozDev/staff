from rest_framework.settings import api_settings


class PermissionByAction(object):
    permission_classes_by_action: dict = {
        'create': api_settings.DEFAULT_PERMISSION_CLASSES,
        'list': api_settings.DEFAULT_PERMISSION_CLASSES,
        'update': api_settings.DEFAULT_PERMISSION_CLASSES,
        'retrieve': api_settings.DEFAULT_PERMISSION_CLASSES,
        'destroy': api_settings.DEFAULT_PERMISSION_CLASSES,
    }

    def get_permissions(self):
        permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

        if self.action == 'partial_update':
            permission_classes = self.permission_classes_by_action['update']
        else:
            permission_classes = self.permission_classes_by_action[self.action]


        return [permission() for permission in permission_classes]