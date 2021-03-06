# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from logging import debug

from django.conf.urls import url
from django.db.models import Count
from django.forms import ChoiceField
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, FormView, CreateView, TemplateView
from character.forms import *
from character.models import *


class CharacterCreateView (CreateView):
    model = Character
    form_class = CharacterBasicForm
    template_name = "character/character_basic.html"

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            for attribute in Attribute.objects.all():
                ca = CharacterAttribute(
                    attribute=attribute,
                    character=self.object,
                    points=5)
                ca.save()
            for skill in Skill.objects.all():
                cs = CharacterSkill(
                    skill=skill,
                    character=self.object,
                    points=0
                )
                cs.save()
            for characterskill in CharacterSkill.objects.all():
                for proficiency in Proficiency.objects.filter(skill=characterskill.skill):
                    cp = CharacterProficiency(
                        characterskill=characterskill,
                        proficiency=proficiency,
                        acquired=False
                    )
                    cp.save()
            return response

    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})


class CharacterListView (ListView):
    model = Character
    template_name = "character/character_list.html"
    fields = '__all__'


class CharacterBasicView (UpdateView):
    model = Character
    form_class = CharacterBasicForm
    template_name = "character/character_detail.html"
    success_url = reverse_lazy('character_basic')


class CharacterAttributeView (UpdateView):
    model = Character
    form_class = CharacterAttributeFormset
    template_name = "character/characterattribute.html"
    success_url = reverse_lazy('character_attribute')

    def get_success_url(self):
        return reverse_lazy('character_attribute', {"pk": self.object})


class CharacterDetailView (UpdateView):
    model = Character
    form_class = CharacterBasicForm
    template_name = "character/character_detail.html"

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
        form = CharacterBasicForm(request.POST, instance=self.object)
        attribute_formset = CharacterAttributeFormset (request.POST,
                                                       instance=self.object,
                                                       prefix='character_attribute')
        skill_formset = CharacterSkillFormset(request.POST,
                                              instance=self.object,
                                              prefix='characterskill')
        proficiency_formsets = {}
        for characterskill in CharacterSkill.objects.filter(character=self.object.pk):
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
                                                                               prefix=characterclass)
        if self.form_valid(form, attribute_formset, skill_formset, proficiency_formsets, schtick_formset, flaw_formset,
                           characterclass_formset, classentry_formsets):
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
        context = super(CharacterDetailView, self).get_context_data(**kwargs)
        context['character_proficiency_formsets'] = {}
        if self.request.POST:
            context['form'] = CharacterBasicForm(self.request.POST, instance=self.object)
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
                                                                                 prefix=character_class)
                for csform in context['character_classentry_formsets'][character_class]:
                    csform.fields['classentry'].queryset = \
                        ClassEntry.objects.filter(characterclass=character_class.characterclass,
                                                  level_startswith=character_class.level)
        else:
            context['form'] = CharacterBasicForm(instance=context['character'])
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
                    CharacterClassentryFormset(instance=character_class, prefix=character_class)
                for csform in context['character_classentry_formsets'][character_class]:
                    csform.fields['classentry'].queryset = \
                        ClassEntry.objects.filter(characterclass=character_class.characterclass,
                                                  level__startswith=character_class.level)

        return context

    def form_valid(self, form, attribute_formset, skill_formset, proficiency_formsets, schtick_formset,
                     flaw_formset, characterclass_formset, classentry_formsets):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.object = self.get_object()
        valid = False
        if form.has_changed() and form.is_valid():
            valid = True
            form.save()
        if attribute_formset.has_changed() and attribute_formset.is_valid():
            valid = True
            attribute_formset.save()
        if skill_formset.has_changed() and skill_formset.is_valid():
            valid = True
            skill_formset.save()
        for characterskill in CharacterSkill.objects.filter(character=self.object):
            pfc = proficiency_formsets[characterskill]
            for single in pfc:
                if single and single.has_changed() and single.is_valid():
                    valid = True
                    single.save()
        if schtick_formset.has_changed():
            if schtick_formset.is_valid():
                valid = True
                schtick_formset.save()
            else:
                not_valid = " Schtick"
        if flaw_formset.has_changed():
            if flaw_formset.is_valid():
                valid = True
                flaw_formset.save()
            else:
                not_valid += " Flaw"
        if characterclass_formset.is_valid():
            valid = True
            characterclass_formset.save()
        else:
            not_valid += " Class"

        for characterclass in CharacterCharacterClass.objects.filter(character=self.object):
            if characterclass.characterclassentry_set is not None:
                cef = classentry_formsets[characterclass]
                for single in cef:
                    if single.is_valid() and single.has_changed():
                        valid = True
                        single.save()
        if valid:
            errors = {}
            self.errors=errors
            return HttpResponseRedirect(self.get_success_url())
        else:
            return False

    def form_invalid(self, form, attribute_formset, skill_formset, proficiency_formsets, schtick_formset,
                     flaw_formset, characterclass_formset, classentry_formsets):
        return self.render_to_response(self.get_context_data())

    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})


class CharacterResetSkillView (CharacterDetailView):

    def reset_skills(self):
        for characterskill in CharacterSkill.objects.filter(character=self.kwargs['pk']):
            for proficiency in CharacterProficiency.objects.filter(characterskill=characterskill):
                print(proficiency)
                proficiency.delete()
        for characterskill in CharacterSkill.objects.all():
            for proficiency in Proficiency.objects.filter(skill=characterskill.skill):
                cp = CharacterProficiency(
                    characterskill=characterskill,
                    proficiency=proficiency,
                    acquired=False
                )
                cp.save()

    def get(self, request, *args, **kwargs):
        self.reset_skills()
        return super().get(request, *args, **kwargs)


class CharacterResetSkillSingleView(CharacterDetailView):
    def reset_skill(self):
            cs = self.kwargs['charskill']
            charskill = CharacterSkill.objects.get(pk=cs)
            charproficiency = CharacterProficiency.objects.filter(characterskill=charskill)
            proficiency = Proficiency.objects.filter(skill=charskill.skill)
            print(charproficiency)
            for old_cp in charproficiency:
                old_cp.delete()
            print(proficiency)
            for item in proficiency:
                cp = CharacterProficiency(
                    characterskill=charskill,
                    proficiency=item,
                    acquired=False
                )
                cp.save()

    def get(self, request, *args, **kwargs):
        self.reset_skill()
        return super().get(request, *args, **kwargs)


class CharacterSchtickView (UpdateView):
    model = Character
    form_class = CharacterSchtickFormset
    template_name = "character/characterattribute.html"
    success_url = reverse_lazy('character_attribute')


class CharacterFlawView (FormView):
    form_class = CharacterFlawFormset
    template_name = "character/characterattribute.html"
    success_url = reverse_lazy('character_flaw')
