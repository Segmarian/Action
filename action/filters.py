import django_filters

from action.forms import ActionCheckboxSelectMultiple
from action.models import Schtick, Flaw, CharacterClass, Modifier, Prereq, SchtickType, ClassEntry


class ActionMultipleChoiceFilter (django_filters.ModelMultipleChoiceFilter):
    class Meta:
        model = Schtick


class SchtickFilter(django_filters.FilterSet):

    class Meta:
        model = Schtick
        fields = ['name', 'tier', 'cost', 'description', 'req', 'type__name',  'type']
    name = django_filters.CharFilter(lookup_expr='icontains')
    type__name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    req = ActionMultipleChoiceFilter(queryset=Prereq.objects.all(),
                                     widget=ActionCheckboxSelectMultiple,
                                     required=False,
                                     )
    type = ActionMultipleChoiceFilter(queryset=SchtickType.objects.all(),
                                      widget=ActionCheckboxSelectMultiple,
                                      )


class FlawFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Flaw
        fields = ['name', 'value']


class SchtickTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SchtickType
        fields = ['name']


class CharClassFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CharacterClass
        fields = ['name', 'schtick_list']


class ClassEntryFilter(django_filters.FilterSet):
    characterclass = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ClassEntry
        fields = ['characterclass', 'level', 'schtick']