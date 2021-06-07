from django import template

from action.models import Proficiency
from character.models import CharacterProficiency

register = template.Library()


@register.filter
def classname(obj):
    return obj.__class__.__name__


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def sort_by(queryset, order):
    return queryset.order_by(order)

@register.simple_tag
def get_verbose_name(object,field):
    return object._meta.get_field(field).verbose_name