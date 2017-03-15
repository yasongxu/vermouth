import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag
def active(request, pattern):
    print("-----")
    print(request)
    print(pattern)
    if re.search(pattern, request.path):
        return 'current-menu-item'
    return ''


