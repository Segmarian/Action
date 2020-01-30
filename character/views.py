# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.forms import ModelMultipleChoiceField
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from character.models import *


class CharacterListView (ListView):
    model = Character
    template = "templates/character_list.html"
    fields = '__all__'


class CharacterUpdateView (UpdateView):
    model = Character
    template = "templates/character_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('character_detail')

    def get_success_url(self):
        messages.success(self.request, '%s updated' % self.request.POST["character"].name)
        return reverse_lazy('character_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chosen_character = context['pk']
        context['form'].fields['character_skill'] = \
            ModelMultipleChoiceField(
                CharacterSkill.objects.filter(character=chosen_character),
                required=False
            )
        context['form'].fields['character_attributes'] = \
            ModelMultipleChoiceField(
                CharacterAttribute.objects.filter(character=chosen_character),
                required=False
            )
        context['form'].fields['character_skills'] = \
            ModelMultipleChoiceField(
                CharacterSkill.objects.filter(character=chosen_character),
                required=False
            )
        context['form'].fields['character_schticks'] = \
            ModelMultipleChoiceField(
                CharacterSchtick.objects.filter(character=chosen_character),
                required=False
            )
        context['form'].fields['character_proficiencies'] = \
            ModelMultipleChoiceField(
                CharacterProficiency.objects.filter(character=chosen_character),
                required=False
            )
        context['form'].fields['character_flaws'] = \
            ModelMultipleChoiceField(
                CharacterFlaw.objects.filter(character=chosen_character),
                required=False
            )

        return context
