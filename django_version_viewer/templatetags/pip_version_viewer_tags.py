from pydoc import locate

from django.conf import settings
from django import template


register = template.Library()
accessor_class = locate(
    getattr(settings, 'ACCESSOR_CLASS_PATH', 'django_version_viewer.mixins.Accessor'))
accessor = accessor_class()


@register.inclusion_tag('version_viewer.html', takes_context=True)
def show_pip_package_versions(context):
    if accessor.allow_access(request=context['request']):
        return {'allow': True}
    else:
        return {'allow': False}
