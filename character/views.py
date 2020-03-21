# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, FormView
from character.forms import CharacterSkillFormset, CharacterSchtickFormset, CharacterFlawFormset, \
    CharacterAttributeFormset, CharacterProficiencyFormset, CharacterSkillForm, CharacterProficiencyForm, \
    CharacterDetailForm, CharacterAttributeForm, CharacterClassentryFormset, CharacterClassFormset
from character.models import *


class CharacterListView (ListView):
    model = Character
    template_name = "character/character_list.html"
    fields = '__all__'


class CharacterUpdateView (UpdateView):
    model = Character
    form_class = CharacterDetailForm
    template_name = "character/character_detail.html"
    success_url = reverse_lazy('character_detail')


class CharacterAttributeView (UpdateView):
    model = Character
    form_class = CharacterAttributeFormset
    template_name = "character/characterattribute.html"
    success_url = reverse_lazy('characterattribute')

    def get_success_url(self):
        return reverse_lazy('character_attribute', {"pk": self.object})


class CharacterSkillView (UpdateView):
    model = Character
    form_class = CharacterDetailForm
    template_name = "character/characterskill.html"

    def get(self, request, *args, **kwargs):
        # The Character we're editing:
        self.object = self.get_object(queryset=Character.objects.all())
        context = self.get_context_data()
        context['skill_formset'] = context['character_skill_formset']
        context['attribute_formset'] = context['character_attribute_formset']
        context['proficiency_formsets'] = context['character_proficiency_formsets']
        context['schtick_formset'] = context['character_schtick_formset']
        context['flaw_formset'] = context['character_flaw_formset']
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CharacterDetailForm(request.POST, instance=self.object)
        attribute_formset = CharacterAttributeFormset (request.POST,
                                                       instance=self.object,
                                                       prefix='characterattribute')
        skill_formset = CharacterSkillFormset(request.POST,
                                              instance=self.object,
                                              prefix='characterskill')
        proficiency_formsets = {}
        for characterskill in CharacterSkill.objects.filter(character=self.object):
            proficiency_formsets[characterskill] = CharacterProficiencyFormset(request.POST,
                                                                               instance=characterskill,
                                                                               prefix=characterskill.skill.name)
        schtick_formset = CharacterSchtickFormset(request.POST,
                                                  instance=self.object,
                                                  prefix='characterschtick')
        flaw_formset = CharacterFlawFormset(request.POST,
                                            instance=self.object,
                                            prefix='characterflaw')
        characterclass_formset = CharacterClassFormset(request.POST,
                                                       instance=self.object,
                                                       prefix='characterclass')
        classentry_formsets = {}
        for characterclass in CharacterCharacterClass.objects.filter(character=self.object):
            classentry_formsets[characterclass] = CharacterClassentryFormset(request.POST,
                                                                               instance=characterclass,
                                                                               prefix=characterclass.characterclass.name)
        if self.form_valid(form, attribute_formset, skill_formset, proficiency_formsets, schtick_formset, flaw_formset):
            return self.form_valid(form,
                                   attribute_formset,
                                   skill_formset,
                                   proficiency_formsets,
                                   schtick_formset,
                                   flaw_formset,
                                   characterclass_formset,
                                   classentry_formsets)
        else:
            return self.form_invalid(form,
                                     attribute_formset,
                                     skill_formset,
                                     proficiency_formsets,
                                     schtick_formset,
                                     flaw_formset,
                                     characterclass_formset,
                                     classentry_formsets)

    def get_context_data(self, **kwargs):
        context = super(CharacterSkillView, self).get_context_data(**kwargs)
        context['character_proficiency_formsets'] = {}
        if self.request.POST:
            context['form'] = CharacterDetailForm(self.request.POST, instance=self.object)
            context['character_attribute_formset'] = CharacterAttributeFormset(self.request.POST,
                                                                               instance=self.object,
                                                                               prefix='characterattribute')
            context['character_skill_formset'] = CharacterSkillFormset(self.request.POST,
                                                                       instance=self.object,
                                                                       prefix='characterskill')
            for character_skill in CharacterSkill.objects.filter(character=context['character']):
                context['character_proficiency_formsets'][character_skill] = \
                    CharacterProficiencyFormset(self.request.POST,
                                                instance=character_skill,
                                                prefix=character_skill.skill.name)
                for csform in context['character_proficiency_formsets'][character_skill]:
                    csform.fields['proficiency'].queryset = \
                        Proficiency.objects.filter(skill=character_skill.skill)
            context['character_schtick_formset'] = CharacterSchtickFormset(self.request.POST,
                                                                           instance=self.object,
                                                                           prefix='characterschtick')
            context['character_flaw_formset'] = CharacterFlawFormset(self.request.POST,
                                                                     instance=context['character'],
                                                                     prefix='characterflaw')
            context['character_characterclass_formset'] = CharacterClassFormset(self.request.POST,
                                                                                instance=self.object,
                                                                                prefix='characterclass')
            context['character_classentry_formsets']={}
            for character_class in CharacterCharacterClass.objects.filter(character=context['character']):
                context['character_classentry_formsets'][character_class] = CharacterClassentryFormset(self.request.POST,
                                                                                 instance=character_class,
                                                                                 prefix=character_class.characterclass.name)
        else:
            context['form'] = CharacterDetailForm(instance=context['character'])
            context['character_attribute_formset'] = CharacterAttributeFormset(instance=context['character'],
                                                                               prefix='characterattribute')
            context['character_skill_formset'] = CharacterSkillFormset(instance=context['character'],
                                                                       prefix='characterskill')
            for character_skill in CharacterSkill.objects.filter(character=context['character']):
                context['character_proficiency_formsets'][character_skill] = \
                    CharacterProficiencyFormset(prefix=character_skill.skill.name, instance=character_skill)
                for csform in context['character_proficiency_formsets'][character_skill]:
                    csform.fields['proficiency'].queryset = \
                        Proficiency.objects.filter(skill=character_skill.skill)
            context['character_schtick_formset'] = CharacterSchtickFormset(instance=context['character'],
                                                                           prefix='characterschtick')
            context['character_flaw_formset'] = CharacterFlawFormset(instance=context['character'],
                                                                     prefix='characterflaw')
            context['character_characterclass_formset'] = CharacterClassFormset(instance=self.object,
                                                                                prefix='characterclass')
            context['character_classentry_formsets']={}
            for character_class in CharacterCharacterClass.objects.filter(character=context['character']):
                context['character_classentry_formsets'][character_class] = \
                    CharacterClassentryFormset(instance=self.object, prefix=character_class.characterclass.name)

        return context

    def form_valid(self, form, attribute_formset, skill_formset, proficiency_formsets, schtick_formset,
                     flaw_formset, characterclass_formset, classentry_formsets):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.object = self.get_object()
        valid = False
        if form.is_valid():
            valid = True
            form.save()
        if attribute_formset.is_valid():
            valid = True
            attribute_formset.save()
        if skill_formset.is_valid():
            valid = True
            skill_formset.save()
        for characterskill in CharacterSkill.objects.filter(character=self.object):
            pfc = proficiency_formsets[characterskill]
            if pfc.is_valid():
                valid = True
                pfc.save()
        if schtick_formset.is_valid():
            valid = True
            schtick_formset.save()
        if flaw_formset.is_valid():
            valid = True
            flaw_formset.save()
        if characterclass_formset.is_valid():
            valid=True
            characterclass_formset.save()
        for characterclass in CharacterCharacterClass.objects.filter(character=self.object):
            cef = classentry_formsets[characterclass]
            if cef.is_valid():
                valid = True
                cef.save()
        if valid:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return False

    def form_invalid(self, form, attribute_formset, skill_formset, proficiency_formsets, schtick_formset,
                     flaw_formset, characterclass_formset, classentry_formsets):
        return self.render_to_response(self.get_context_data())

    def get_success_url(self):
        return reverse('character_skill', kwargs={'pk': self.object.pk})


class CharacterSchtickView (UpdateView):
    model = Character
    form_class = CharacterSchtickFormset
    template_name = "character/characterattribute.html"
    success_url = reverse_lazy('character_attribute')


class CharacterFlawView (FormView):
    form_class = CharacterFlawFormset
    template_name = "character/characterattribute.html"
    success_url = reverse_lazy('character_flaw')
