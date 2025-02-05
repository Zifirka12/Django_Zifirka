from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


def create_moderator_group():
    # Получаем нужные права
    unpublish_permission = Permission.objects.get(codename="can_unpublish_product")
    delete_permission = Permission.objects.get(codename="delete_product")

    # Создаем группу 'Модератор продуктов'
    moderator_group, created = Group.objects.get_or_create(name="Модератор продуктов")

    # Назначаем группе права
    moderator_group.permissions.add(unpublish_permission, delete_permission)
