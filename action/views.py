# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from action.filters import *
from action.forms import CharacterClassForm, SchtickForm
from action.models import *


class ActionView (TemplateView):
    template_name = "action/index.html"


class CharacterClassListView (FilterView):
    model = CharacterClass
    template_name = "action/characterclass_list.html"
    fields = '__all__'
    filterset_class = CharClassFilter


class CharacterClassUpdateView (UpdateView):
    model = CharacterClass
    template_name = "action/characterclass_detail.html"
    form_class = CharacterClassForm

    def get_success_url(self):
        return reverse_lazy('characterclass_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(CharacterClassUpdateView, self).get_context_data(**kwargs)
        context['class_entries'] = ClassEntry.objects.filter(characterclass=self.object.pk).order_by('level')
        return context


class CharacterClassCreateView (CreateView):
    model = CharacterClass
    template_name = "action/characterclass_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('characterclass_list', )


class ClassEntryListView (FilterView):
    model = ClassEntry
    template_name = "action/classentry.html"
    fields = '__all__'
    filterset_class = ClassEntryFilter


class ClassEntryUpdateView (UpdateView):
    model = ClassEntry
    template_name = "action/classentry_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('classentry_detail', kwargs={'pk': self.object.pk})


class ClassEntryCreateView (CreateView):
    model = ClassEntry
    template_name = "action/classentry_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('classentry_list', )


class ClassEntryCreateFromClassView (ClassEntryCreateView):

    def get_initial(self):
        initial = super().get_initial()
        if 'item' in self.kwargs:
            initial['characterclass'] = self.kwargs['item']
        return initial

    def get_success_url(self):
        return reverse_lazy('classentry_detail', kwargs={'pk': self.object.characterclass.pk})


class SchtickListView (FilterView):
    model = Schtick
    template_name = "action/schtick_list.html"
    fields = '__all__'
    filterset_class = SchtickFilter


class SchtickCreateView (CreateView):
    model = Schtick
    form_class = SchtickForm
    template_name = "action/schtick_detail.html"
    success_url = reverse_lazy('schticks', )


class SchtickUpdateView (UpdateView):
    model = Schtick
    form_class = SchtickForm
    template_name = "action/schtick_detail.html"

    def get_success_url(self):
        return reverse_lazy('schtick_detail', kwargs={"pk": self.object.pk})


class SchtickDeleteView (DeleteView):
    model = Schtick
    template_name = "action/schtick_delete.html"
    success_url = reverse_lazy('schticks')


class FlawListView (FilterView):
    model = Flaw
    template_name = "action/flaw_list.html"
    fields = '__all__'
    filterset_class = FlawFilter


class FlawCreateView (CreateView):
    model = Flaw
    template_name = "action/flaw_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('flaws', )


class FlawUpdateView (UpdateView):
    model = Flaw
    template_name = "action/flaw_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('flaw_detail', kwargs={"pk": self.object.pk})


class SchtickTypeListView (FilterView):
    model = SchtickType
    template_name = "action/schticktype_list.html"
    fields = '__all__'
    filterset_class = SchtickTypeFilter


class SchtickTypeUpdateView (UpdateView):
    model = SchtickType
    template_name = "action/schticktype_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('schticktype_detail', kwargs={"pk": self.object.pk})


class SchtickTypeCreateView (CreateView):
    model = SchtickType
    template_name = "action/schticktype_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('schticktypes', )


class SchtickTypeCreateReturnView (CreateView):
    model = SchtickType
    template_name = "action/schticktype_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('charclass_create', )


class PrereqListView (ListView):
    model = Prereq
    template_name = "action/prereq_list.html"
    fields = '__all__'


class PrereqCreateView (CreateView):
    model = Prereq
    template_name = "action/prereq_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('prereqs')


class PrereqUpdateView (UpdateView):
    model = Prereq
    template_name = "action/prereq_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('prereq_detail', kwargs={"pk": self.object.pk})


class PrereqDeleteView (DeleteView):
    model = Prereq
    template_name = "action/prereq_delete.html"
    success_url = reverse_lazy('prereqs')


class SchtickTypeDeleteView (DeleteView):
    model = SchtickType
    template_name = "action/schticktype_delete.html"
    success_url = reverse_lazy('schticktypes')


class CampaignListView (ListView):
    model = Campaign
    template_name = "action/campaign_list.html"
    fields = '__all__'


class CampaignCreateView (CreateView):
    model = Campaign
    template_name = "action/campaign_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('campaigns')


class CampaignUpdateView (UpdateView):
    model = Campaign
    template_name = "action/campaign_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('campaign_detail', kwargs={"pk": self.object.pk})