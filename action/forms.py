from django import forms
from django.forms import *
from django import forms

from action.models import ClassEntry, CharacterClass, SchtickType, Schtick, Prereq

from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class ClassEntryChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return self.classentry.schtick + self.classentry.flaw


class ActionCheckboxSelectMultiple(CheckboxSelectMultiple):

    template_name = 'action/widgets/checkbox_select.html'
    option_template_name = 'action/widgets/checkbox_option.html'


class PrereqModelMultipleChoiceField(ModelMultipleChoiceField):
    class Meta:
        model = Prereq

    def label_from_instance(self, obj):
        return obj.__str__


class SchtickListModelMultipleChoiceField(ModelMultipleChoiceField):
    class Meta:
        model = SchtickType

    def label_from_instance(self, obj):
        return obj.name


class SchtickForm(ModelForm):
    class Meta:
        model = Schtick
        fields = ('name', 'cost', 'tier', 'req', 'description', 'type',)
    req = PrereqModelMultipleChoiceField(queryset=Prereq.objects.all(),
                                         widget=ActionCheckboxSelectMultiple,
                                         required=False)
    type = SchtickListModelMultipleChoiceField(queryset=SchtickType.objects.all(),
                                               widget=ActionCheckboxSelectMultiple,
                                               required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CharacterClassForm(ModelForm):
    class Meta:
        model = CharacterClass
        fields = '__all__'


class ClassEntryForm(ModelForm):
    class Meta:
        model = ClassEntry
        fields = '__all__'
    notes = CharField(widget=TextInput(attrs={'style': 'width:350px'}))
    level = ChoiceField(widget=TextInput(attrs={'style': 'width:100px'}))
    default = BooleanField()
    optional = BooleanField()
    divisor = IntegerField(widget=NumberInput(attrs={'style': 'width:40px'}))


ClassEntryFormset = modelformset_factory(ClassEntry, form=ClassEntryForm, extra=1)
