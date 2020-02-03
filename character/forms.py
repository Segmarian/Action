from __future__ import unicode_literals

from django.forms import ModelForm, IntegerField, formset_factory, modelformset_factory, BooleanField

from character.models import Character, CharacterSkill, CharacterProficiency, CharacterAttribute, CharacterFlaw, \
    CharacterSchtick

from django.forms.widgets import CheckboxSelectMultiple

from character.models import *


class CharacterDetailForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'


class CharacterSkillForm(ModelForm):
    class Meta:
        model = CharacterSkill
        fields = ['points']


class CharacterProficiencyForm(ModelForm):
    class Meta:
        model = CharacterProficiency
        fields = ['acquired']
        acquired = BooleanField(widget=CheckboxSelectMultiple)


class CharacterAttributeForm(ModelForm):
    class Meta:
        model = CharacterAttribute
        fields = ['points']


class CharacterFlawForm(ModelForm):
    class Meta:
        model = CharacterFlaw
        fields = ['flaw', 'points']


class CharacterSchtickForm(ModelForm):
    class Meta:
        model = CharacterSchtick
        fields = ['schtick', 'points']

CharacterSkillFormset = modelformset_factory(CharacterSkill, fields = ['skill', 'points'], extra=1)
CharacterProficiencyFormset = modelformset_factory(CharacterProficiency, fields = ['proficiency', 'acquired'], extra=1)
CharacterAttributeFormset = modelformset_factory(CharacterAttribute, fields = ['attribute', 'points'], extra=1)
CharacterSchtickFormset = modelformset_factory(CharacterSchtick, fields = ['schtick', 'points'], extra=1)
CharacterFlawFormset = modelformset_factory(CharacterFlaw, fields = ['flaw', 'points'], extra=1)