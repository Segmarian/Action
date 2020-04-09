from __future__ import unicode_literals

from character.models import *
from django.forms import *


class CharacterBasicForm(ModelForm):

    class Meta:
        model = Character
        fields = ['name', 'points', 'notes']
    name = CharField()
    name.widget.attrs['class'] = 'form-control'
    points = IntegerField()
    points.widget.attrs['class'] = 'form-control'
    notes = CharField(widget=Textarea())
    notes.widget.attrs['class'] = 'form-control'


class CharacterSkillForm(ModelForm):
    class Meta:
        model = CharacterSkill
        fields = ['skill', 'points', 'character']
        widgets = {'character': HiddenInput(),
                   'skill': HiddenInput()}


class CharacterProficiencyForm(ModelForm):
    class Meta:
        model = CharacterProficiency
        fields = ['proficiency', 'acquired', 'characterskill']
        widgets = {'characterskill': HiddenInput(), 'proficiency': HiddenInput(), 'acquired': CheckboxInput()}


class CharacterAttributeForm(ModelForm):
    class Meta:
        model = CharacterAttribute
        fields = ['attribute', 'points']


class CharacterFlawForm(ModelForm):
    class Meta:
        model = CharacterFlaw
        fields = ['flaw', 'points', 'character', 'notes']
        widgets = {'character': HiddenInput(),}


class CharacterSchtickForm(ModelForm):
    class Meta:
        model = CharacterSchtick
        fields = ['schtick', 'points', 'character', 'notes']
        widgets = {'character': HiddenInput()}

    schtick = ModelChoiceField(queryset=Schtick.objects.exclude(type=4).order_by('type__name'))

class CharacterClassForm(ModelForm):
    class Meta:
        model = CharacterClass
        fields = '__all__'
        widgets = {'level': Select()}


class ClassEntryChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return self.classentry.schtick


class ClassEntryForm(ModelForm):
    class Meta:
        model = ClassEntry
        fields = '__all__'
        classentry = ClassEntryChoiceField(queryset=ClassEntry.objects.all(),
                                           to_field_name="classentry")
        level = ChoiceField()


class CharacterClassForm(ModelForm):
    class Meta:
        model = CharacterCharacterClass
        fields = ['character', 'characterclass', 'level']
        widgets = {'character': HiddenInput()}


class CharacterClassentryForm(ModelForm):
    class Meta:
        model = CharacterClassEntry
        fields = ['character_characterclass', 'classentry', 'notes']
        widgets = {'character_characterclass': HiddenInput(),
                   'classentry': Select(attrs={'class': 'col-sm-12'})}


CharacterClassFormset = inlineformset_factory(Character, CharacterCharacterClass, extra=1,
                                              form=CharacterClassForm)
CharacterClassentryFormset = inlineformset_factory(CharacterCharacterClass, CharacterClassEntry, extra=1,
                                                   form=CharacterClassentryForm)
CharacterProficiencyFormset = inlineformset_factory(CharacterSkill, CharacterProficiency, form=CharacterProficiencyForm,
                                                    extra=1)
CharacterSkillFormset = inlineformset_factory(Character, CharacterSkill, extra=1, form=CharacterSkillForm)
CharacterAttributeFormset = inlineformset_factory(Character, CharacterAttribute, form=CharacterAttributeForm, extra=1)
CharacterSchtickFormset = inlineformset_factory(Character, CharacterSchtick, form=CharacterSchtickForm, extra=1)
CharacterFlawFormset = inlineformset_factory(Character, CharacterFlaw, form=CharacterFlawForm, extra=1)