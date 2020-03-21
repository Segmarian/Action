from __future__ import unicode_literals
from django.forms import ModelForm, IntegerField, formset_factory, modelformset_factory, BooleanField, \
    inlineformset_factory, CharField

from action.models import CharacterClass
from character.models import Character, CharacterSkill, CharacterProficiency, CharacterAttribute, CharacterFlaw, \
    CharacterSchtick

from django.forms import CheckboxSelectMultiple, Textarea, TextInput, NumberInput, HiddenInput, ChoiceField, \
    BaseInlineFormSet

from character.models import *


class CharacterDetailForm(ModelForm):

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
        widgets = {'characterskill': HiddenInput()}


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
        widgets = {'character': HiddenInput(),}


class CharacterClassForm(ModelForm):
    class Meta:
        model = CharacterClass
        fields = '__all__'


class ClassEntryForm(ModelForm):
    class Meta:
        model = ClassEntry
        fields = '__all__'


class CharacterClassForm(ModelForm):
    class Meta:
        model = CharacterCharacterClass
        fields = ['character', 'characterclass']
        widgets = {'character': HiddenInput()}


class CharacterClassentryForm(ModelForm):
    class Meta:
        model = CharacterClassEntry
        fields = ['character', 'classentry']
        widgets = {'character': HiddenInput()}


CharacterClassFormset = inlineformset_factory(Character, CharacterCharacterClass, extra=1,
                                              form=CharacterClassForm)
CharacterClassentryFormset = inlineformset_factory(Character, CharacterClassEntry, extra=1,
                                                   form=CharacterClassentryForm)
CharacterProficiencyFormset = inlineformset_factory(CharacterSkill, CharacterProficiency, form=CharacterProficiencyForm, extra=1)
CharacterSkillFormset = inlineformset_factory(Character, CharacterSkill, extra=1, form=CharacterSkillForm)
CharacterAttributeFormset = inlineformset_factory(Character, CharacterAttribute, form=CharacterAttributeForm, extra=1)
CharacterSchtickFormset = inlineformset_factory(Character, CharacterSchtick, form=CharacterSchtickForm, extra=1)
CharacterFlawFormset = inlineformset_factory(Character, CharacterFlaw, form=CharacterFlawForm, extra=1)