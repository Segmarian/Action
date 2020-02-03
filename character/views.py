# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from character.forms import CharacterSkillFormset, CharacterSchtickFormset, CharacterFlawFormset, CharacterAttributeFormset, \
    CharacterProficiencyFormset, CharacterSkillForm, CharacterProficiencyForm
from character.models import *


class CharacterListView (ListView):
    model = Character
    template_name = "character/character_list.html"
    fields = '__all__'


class CharacterUpdateView (UpdateView):
    model = Character
    template_name = "character/character_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('character_detail')

    def get_success_url(self):
        messages.success(self.request, '%s updated' % self.request.POST["character"].name)
        return reverse_lazy('character_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        '''chosen_character = context['pk']'''
        '''context['character_skill_form'] = CharacterSkillFormset()'''
        context['character_attribute_form'] = CharacterAttributeFormset()
        context['skills']={}
        skill_form = {}
        for skill in Skill.objects.all():
            skill_form[skill.name] = {skill.name, CharacterSkillForm()}
            for proficiency in Proficiency.objects.filter(skill=skill):
                skill_form[proficiency.name] = {proficiency.name, CharacterProficiencyForm()}
        context['skills'] = skill_form
        '''context['character_skill_form']['character_proficiency_form'] = CharacterProficiencyFormset()'''
        context['character_schtick_form'] = CharacterSchtickFormset()
        context['character_flaw_form'] = CharacterFlawFormset()

        return context
